import os
import requests
from requests_toolbelt import MultipartEncoder
import json
import logging

FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
PAGE_ACCESS_TOKEN = os.environ['PAGE_ACCESS_TOKEN']

# Logging
logger = logging.getLogger('app')

def verify_webhook(req):
    if req.args.get("hub.verify_token") == VERIFY_TOKEN:
        return req.args.get("hub.challenge")
    else:
        return "Invalid Webhook Subscription's Verify Token"

def is_user_message(message):
    """Check if the message is a message from the user"""
    return (message.get('message') and
            message['message'].get('text') and
            not message['message'].get("is_echo"))

def get_bot_response(message):
    return "ลูกสมุนไพร่: '{}'".format(message)

def send_message(recipient_id, text):
    """Send a response to Facebook"""
    payload = {
        'message': {
            'text': text
        },
        'recipient': {
            'id': recipient_id
        },
        'notification_type': 'regular'
    }

    auth = {
        'access_token': PAGE_ACCESS_TOKEN
    }

    response = requests.post(
        FB_API_URL,
        params=auth,
        json=payload,
    )

    return response.json()


def send_image(recipient_id, image_path):
    """Send a response to Facebook"""
    # print("image_path = " + image_path)
    payload = {
        'message': '{ "attachment": { "type": "image", "payload": {} } }',
        'filedata': (os.path.basename(image_path), open(image_path, 'rb'), 'image/png'),
        'recipient': '{ "id": ' + recipient_id + ' }',
        'notification_type': 'regular'
    }

    auth = {
        'access_token': PAGE_ACCESS_TOKEN
    }

    multipart_data = MultipartEncoder(payload)
    multipart_header = {
        'Content-Type': multipart_data.content_type
    }

    logger.debug("Send image %s to recipient id %s", recipient_id, image_path)

    return requests.post(FB_API_URL, data=multipart_data,
                     params=auth, headers=multipart_header).json()


def respond(recipient_id, message):
    send_message(recipient_id, message)

def debug_respond(recipient_id, message):
    response = get_bot_response(message)
    send_message(recipient_id, response)
