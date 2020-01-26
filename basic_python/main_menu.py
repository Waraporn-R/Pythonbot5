from linebot.models import *

def main_menu_message():
    json_data = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "carousel",
    "contents": [
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://nuuneoi.com/blog/978/coronavirus.jpg",
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": "| SHOW VIRUS",
              "size": "xl",
              "weight": "bold",
              "wrap": True
            },
            {
              "type": "box",
              "layout": "baseline",
              "margin": "none",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://image.flaticon.com/icons/svg/430/430098.svg",
                  "size": "xs",
                  "aspectRatio": "1:1"
                },
                {
                  "type": "filler"
                },
                {
                  "type": "text",
                  "text": "แสดงข้อมูลไวรัส",
                  "flex": 10,
                  "size": "sm",
                  "weight": "regular",
                  "color": "#A0A0A0",
                  "wrap": True
                }
              ]
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "message",
                "label": "แสดงข้อมูลไวรัส",
                "text": "4"
              },
              "color": "#00AAFF",
              "height": "sm",
              "style": "primary"
            }
          ]
        }
      },
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://nuuneoi.com/blog/978/coronavirus.jpg",
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": "| UPDATE VIRUS",
              "size": "xl",
              "weight": "bold",
              "wrap": True
            },
            {
              "type": "box",
              "layout": "baseline",
              "margin": "none",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://image.flaticon.com/icons/svg/457/457710.svg",
                  "size": "xs",
                  "aspectRatio": "1:1"
                },
                {
                  "type": "filler"
                },
                {
                  "type": "text",
                  "text": "แก้ไขข้อมูลไวรัส",
                  "flex": 10,
                  "size": "sm",
                  "weight": "regular",
                  "color": "#A0A0A0",
                  "wrap": True
                }
              ]
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "message",
                "label": "อัพเดตข้อมูลไวรัส",
                "text": "3"
              },
              "color": "#FFDA00",
              "height": "sm",
              "style": "secondary"
            }
          ]
        }
      },
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://nuuneoi.com/blog/978/coronavirus.jpg",
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": "| ADD VIRUS",
              "size": "xl",
              "weight": "bold",
              "wrap": True
            },
            {
              "type": "box",
              "layout": "baseline",
              "margin": "none",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOtMYU1hM0CKc48K8Zbi7F42765qeM4KEiHtwIoD77ZzgqokY-",
                  "size": "xxs",
                  "aspectRatio": "1:1"
                },
                {
                  "type": "filler"
                },
                {
                  "type": "text",
                  "text": "เพิ่มข้อมูลไวรัสตัวใหม่",
                  "flex": 10,
                  "size": "sm",
                  "weight": "regular",
                  "color": "#A0A0A0",
                  "wrap": True
                }
              ]
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "message",
                "label": "เพิ่มข้อมูลไวรัส",
                "text": "1"
              },
              "height": "sm",
              "style": "primary"
            }
          ]
        }
      },
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://nuuneoi.com/blog/978/coronavirus.jpg",
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": "| DELETE VIRUS",
              "size": "xl",
              "weight": "bold",
              "wrap": True
            },
            {
              "type": "box",
              "layout": "baseline",
              "margin": "none",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSL-CCQKpl-BU5Y5CltGCcLhTTTWr-RlY9t8cKNCjKiLPZDBfuk",
                  "size": "xs",
                  "aspectRatio": "1:1"
                },
                {
                  "type": "filler"
                },
                {
                  "type": "text",
                  "text": "ลบข้อมูลไวรัส",
                  "flex": 10,
                  "size": "sm",
                  "weight": "regular",
                  "color": "#A0A0A0",
                  "wrap": True
                }
              ]
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "message",
                "label": "ลบข้อมูลไวรัส",
                "text": "2"
              },
              "color": "#FF0000",
              "height": "sm",
              "style": "primary"
            }
          ]
        }
      }
    ]
  }
}
    FLEX_TO_REPLY = Base.get_or_new_from_json_dict(json_data,FlexSendMessage)
    return FLEX_TO_REPLY