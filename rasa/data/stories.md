## default greeting
* user.ทักทาย
 - bot.utter.greeting
 - action_slot_reset
## default_thankyou
* user.ขอบคุณ
  - bot.utter.thankyou
  - action_slot_reset
  
##default_about_us
* user.สมุนไพรคืออะไร

##default_about_us
* user.หน้าที่ของบอท
 - bot.utter.default.about_bot
##default_about_us
* user.เกี่ยวกับบอท
 - bot.utter.default.about_bot

## สมุนไพร
* user.สมุนไพร {"herb":""}
 - bot.ask.menu


## ค้นหาชื่อจากรูป_ผิด
* user.ค้นหาสมุนไพรจากรูป
 - bot.ask.photo
* user.ส่งรูปภาพ
 - bot.action.photo_to_name
* user.พบสมุนไพร
 - bot.utter.herb_name
 - bot.validation.herb_name
* user.ไม่
 - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร {"herb":" "}
 - bot.validation.get_data.herb_name
 - action_slot_reset
## ค้นหาชื่อจากรูป_ผิด
* user.ค้นหาสมุนไพรจากรูป
 - bot.ask.photo
* user.ส่งรูปภาพ
 - bot.action.photo_to_name
* user.พบสมุนไพร
 - bot.utter.herb_name
 - bot.validation.herb_name
* user.ไม่
 - bot.ask.get_data
* user.สมุนไพร {"herb":" "}
 - bot.validation.get_data.herb_name
 - action_slot_reset
## ค้นหาชื่อจากรูป_ถูก
* user.ค้นหาสมุนไพรจากรูป
 - bot.ask.photo
* user.ส่งรูปภาพ
 - bot.action.photo_to_name
* user.พบสมุนไพร
 - bot.utter.herb_name
 - bot.validation.herb_name
* user.ใช่
 - bot.utter.thankyou
 - action_slot_reset
## ค้นหาชื่อจากรูป_ไม่พบรูป
* user.ค้นหาสมุนไพรจากรูป
 - bot.ask.photo
* user.ส่งรูปภาพ
 - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
 - bot.utter.herb_name.not_found
 - action_slot_reset

## ค้นหาชื่อจากรูป_ผิด
* user.ส่งรูปภาพ
 - bot.action.photo_to_name
* user.พบสมุนไพร
 - bot.utter.herb_name
 - bot.validation.herb_name
* user.ไม่
 - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร {"herb":" "}
 - bot.validation.get_data.herb_name
 - action_slot_reset
## ค้นหาชื่อจากรูป_ผิด
* user.ส่งรูปภาพ
 - bot.action.photo_to_name
* user.พบสมุนไพร
 - bot.utter.herb_name
 - bot.validation.herb_name
* user.ไม่
 - bot.ask.get_data
* user.สมุนไพร {"herb":" "}
 - bot.validation.get_data.herb_name
 - action_slot_reset
## ค้นหาชื่อจากรูป_ผิด
* user.ส่งรูปภาพ
 - bot.action.photo_to_name
* user.พบสมุนไพร
 - bot.utter.herb_name
 - bot.validation.herb_name
* user.ไม่แน่ใจ
 - bot.utter.thankyou
 - action_slot_reset
## ค้นหาชื่อจากรูป_ถูก
* user.ส่งรูปภาพ
 - bot.action.photo_to_name
* user.พบสมุนไพร
 - bot.utter.herb_name
 - bot.validation.herb_name
* user.ใช่
 - bot.utter.thankyou
 - action_slot_reset
## ค้นหาชื่อจากรูป_ไม่พบรูป
* user.ส่งรูปภาพ
 - bot.action.photo_to_name
* user.ไม่พบสมุนไพร
 - bot.utter.herb_name.not_found
 - action_slot_reset

## ขอดูรูปจากชื่อสมุนไพร
* user.ดูรูปสมุนไพร {"herb": null}
 - bot.ask.name_to_photo.herb_name
* {"herb": " "}
 - bot.action.validate.herb
* user.พบสมุนไพร
 - bot.action.name_to_photo
* user.พบสมุนไพร
 - bot.utter.herb_photo
 - bot.validation.herb_photo
* user.ไม่
 - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร {"herb":" "}
 - bot.validation.get_data.herb_photo
 - action_slot_reset
## ขอดูรูปจากชื่อสมุนไพร
* user.ดูรูปสมุนไพร {"herb": null}
 - bot.ask.name_to_photo.herb_name
* {"herb": " "}
 - bot.action.validate.herb
* user.พบสมุนไพร
 - bot.action.name_to_photo
* user.พบสมุนไพร
 - bot.utter.herb_photo
 - bot.validation.herb_photo
* user.ไม่
 - bot.ask.get_data
* {"herb":" "}
 - bot.validation.get_data.herb_photo
 - action_slot_reset
## ขอดูรูปจากชื่อสมุนไพร
* user.ดูรูปสมุนไพร {"herb": null}
 - bot.ask.name_to_photo.herb_name
* {"herb": " "}
 - bot.action.validate.herb
* user.พบสมุนไพร
 - bot.action.name_to_photo
* user.พบสมุนไพร
 - bot.utter.herb_photo
 - bot.validation.herb_photo
* user.ไม่แน่ใจ
 - bot.utter.thankyou
 - action_slot_reset
## ขอดูรูปจากชื่อสมุนไพร
* user.ดูรูปสมุนไพร {"herb": null}
 - bot.ask.name_to_photo.herb_name
* {"herb": " "}
 - bot.action.validate.herb
* user.พบสมุนไพร
 - bot.action.name_to_photo
* user.พบสมุนไพร
 - bot.utter.herb_photo
 - bot.validation.herb_photo
* user.ใช่
 - bot.utter.thankyou
 - action_slot_reset
## ขอดูรูปจากชื่อสมุนไพร_ผิด
* user.ดูรูปสมุนไพร {"herb":" "}
 - bot.action.validate.herb
* user.พบสมุนไพร
 - bot.action.name_to_photo
* user.พบสมุนไพร
 - bot.utter.herb_photo
 - bot.validation.herb_photo
* user.ไม่
 - bot.ask.get_data
* user.แจ้งข้อมูลสมุนไพร {"herb":" "}
 - bot.validation.get_data.herb_photo
 - action_slot_reset
## ขอดูรูปจากชื่อสมุนไพร_ผิด
* user.ดูรูปสมุนไพร {"herb":" "}
 - bot.action.validate.herb
* user.พบสมุนไพร
 - bot.action.name_to_photo
* user.พบสมุนไพร
 - bot.utter.herb_photo
 - bot.validation.herb_photo
* user.ไม่แน่ใจ
 - bot.utter.thankyou
 - action_slot_reset
## ขอดูรูปจากชื่อสมุนไพร_ถูก
* user.ดูรูปสมุนไพร {"herb":" "}
 - bot.action.validate.herb
* user.พบสมุนไพร
 - bot.action.name_to_photo
* user.พบสมุนไพร
 - bot.utter.herb_photo
 - bot.validation.herb_photo
* user.ใช่
 - bot.utter.thankyou
 - action_slot_reset
## ขอดูรูปจากชื่อสมุนไพรไม่พบ
* user.ดูรูปสมุนไพร {"herb":" "}
 - bot.action.validate.herb
* user.ไม่พบสมุนไพร
 - bot.ask.validate.herb
* user.ใช่
 - bot.action.name_to_photo
* user.พบสมุนไพร
 - bot.utter.herb_photo
 - bot.validation.herb_photo
* user.ใช่
 - bot.utter.thankyou
 - action_slot_reset
## ขอดูรูปจากชื่อสมุนไพรไม่พบ
* user.ดูรูปสมุนไพร {"herb":" "}
 - bot.action.validate.herb
* user.ไม่พบสมุนไพร
 - bot.ask.validate.herb
* user.ใช่
 - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
 - bot.utter.herb_photo.not_found
 - action_slot_reset
## ขอดูรูปจากชื่อสมุนไพรไม่พบ
* user.ดูรูปสมุนไพร {"herb":" "}
 - bot.action.validate.herb
* user.ไม่พบสมุนไพร
 - bot.ask.validate.herb
* user.ไม่ใช่
 - bot.ask.get_data
* user.สมุนไพร {"herb": " "}
 - bot.validation.get_data.herb_photo
 - action_slot_reset
## ขอดูรูปจากชื่อสมุนไพร
* user.ดูรูปสมุนไพร {"herb": null}
 - bot.ask.name_to_photo.herb_name
* {"herb": " "}
 - bot.action.validate.herb
* user.พบสมุนไพร
 - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
 - bot.utter.herb_photo.not_found
 - action_slot_reset
## ขอดูรูปจากชื่อสมุนไพรไม่พบ
* user.ดูรูปสมุนไพร {"herb":" "}
 - bot.action.validate.herb
* user.พบสมุนไพร
 - bot.action.name_to_photo
* user.ไม่พบสมุนไพร
 - bot.utter.herb_photo.not_found
 - action_slot_reset
 
## ข้อมูลทั่วไป
* user.สรรพคุณสมุนไพร {"herb": null}
 - bot.ask.name_to_benefit.herb_name
* {"herb":" "}
 - bot.action.name_to_benefit
* user.พบสมุนไพร
 - bot.utter.benefit
 - action_slot_reset
## ข้อมูลทั่วไป
* user.สรรพคุณสมุนไพร {"herb": null}
 - bot.ask.name_to_benefit.herb_name
* user.สมุนไพร {"herb":" "}
 - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
 - bot.ask.validate.herb
* user.ไม่
 - bot.utter.benefit.not_found
 - action_slot_reset
## ข้อมูลทั่วไป
* user.สรรพคุณสมุนไพร {"herb": null}
 - bot.ask.name_to_benefit.herb_name
* {"herb":" "}
 - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
 - bot.ask.validate.herb
* user.ไม่แน่ใจ
 - bot.utter.thankyou
 - action_slot_reset
## ข้อมูลทั่วไป
* user.สรรพคุณสมุนไพร {"herb": null}
 - bot.ask.name_to_benefit.herb_name
* user.สมุนไพร {"herb":" "}
 - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
 - bot.ask.validate.herb
* user.ใช่
 - bot.utter.benefit
 - action_slot_reset
## ข้อมูลทั่วไป_เจอ
* user.สรรพคุณสมุนไพร {"herb":" "}
 - bot.action.name_to_benefit
* user.พบสมุนไพร
 - bot.utter.benefit
 - action_slot_reset
## ข้อมูลทั่วไป_ไม่เจอ
* user.สรรพคุณสมุนไพร {"herb":" "}
 - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
 - bot.ask.validate.herb
* user.ใช่
 - bot.utter.benefit
 - action_slot_reset
## ข้อมูลทั่วไป_ไม่เจอ
* user.สรรพคุณสมุนไพร {"herb":" "}
 - bot.action.name_to_benefit
* user.ไม่พบสมุนไพร
 - bot.ask.validate.herb
* user.ไม่
 - bot.utter.benefit.not_found
 - action_slot_reset

## ข้อมูลทั่วไป_เจอ
* user.ดูข้อมูลทั่วไปของสมุนไพร {"herb": null}
 - bot.ask.name_to_detail.herb_name
* {"herb":" "}
 - bot.action.name_to_detail
* user.พบสมุนไพร
 - bot.utter.detail
 - action_slot_reset
## ข้อมูลทั่วไป_ไม่เจอ
* user.ดูข้อมูลทั่วไปของสมุนไพร {"herb": null}
 - bot.ask.name_to_detail.herb_name
* {"herb":" "}
 - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
 - bot.ask.validate.herb
* user.ไม่
 - bot.utter.detail.not_found
 - action_slot_reset
## ข้อมูลทั่วไป_ไม่เจอ
* user.ดูข้อมูลทั่วไปของสมุนไพร {"herb": null}
 - bot.ask.name_to_detail.herb_name
* {"herb":" "}
 - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
 - bot.ask.validate.herb
* user.ใช่
 - bot.utter.detail
 - action_slot_reset
## ข้อมูลทั่วไป_เจอ
* user.ดูข้อมูลทั่วไปของสมุนไพร {"herb":" "}
 - bot.action.name_to_detail
* user.พบสมุนไพร
 - bot.utter.detail
 - action_slot_reset
## ข้อมูลทั่วไป_ไม่เจอ
* user.ดูข้อมูลทั่วไปของสมุนไพร {"herb":" "}
 - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
 - bot.ask.validate.herb
* user.ใช่
 - bot.utter.detail
 - action_slot_reset
## ข้อมูลทั่วไป_ไม่เจอ
* user.ดูข้อมูลทั่วไปของสมุนไพร {"herb":" "}
 - bot.action.name_to_detail
* user.ไม่พบสมุนไพร
 - bot.ask.validate.herb
* user.ไม่
 - bot.utter.detail.not_found
 - action_slot_reset

## แนะนำสมุนไพร_พบสมุนไพร
* user.หาสมุนไพรจากสรรพคุณ {"feature": null}
 - bot.ask.feature_to_herb.feature
* {"feature": "ผิวแห้ง"}
 - bot.action.feature_to_herb
* user.พบสมุนไพร
 - bot.utter.herb_feature
 - bot.default.ask_more
 - action_slot_reset
## แนะนำสมุนไพร_ไม่พบสมุนไพร
* user.หาสมุนไพรจากสรรพคุณ {"feature": null}
 - bot.ask.feature_to_herb.feature
* {"feature": "ผิวแห้ง"}
 - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
 - bot.utter.herb_feature.not_found
 - bot.default.ask_more
 - action_slot_reset
## แนะนำสมุนไพร_พบสมุนไพร
* user.หาสมุนไพรจากสรรพคุณ {"feature":"ผิวแห้ง"}
 - bot.action.feature_to_herb
* user.พบสมุนไพร
 - bot.utter.herb_feature
 - bot.default.ask_more
 - action_slot_reset
## แนะนำสมุนไพร_พบสมุนไพร
* user.หาสมุนไพรจากสรรพคุณ {"feature":"ผิวแห้ง"}
 - bot.action.feature_to_herb
* user.ไม่พบสมุนไพร
 - bot.utter.herb_feature.not_found
 - bot.default.ask_more
 - action_slot_reset

## แหล่งข้อมูล_สมุนไพร
* user.แหล่งข้อมูลสมุนไพร
 - bot.action.source_website
## แหล่งข้อมูล_สมุนไพร
* user.แหล่งข้อมูลสมุนไพร.thai_med
 - bot.action.source_website.thai_med
## แหล่งข้อมูล_สมุนไพร
* user.แหล่งข้อมูลสมุนไพร.mix
 - bot.action.source_website.mix
## แหล่งข้อมูล_สมุนไพร
* user.แหล่งข้อมูลสมุนไพร.thai_sci
 - bot.action.source_website.thai_sci