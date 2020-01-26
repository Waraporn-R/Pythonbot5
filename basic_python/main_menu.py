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
  

def greeting_message():
  json_data = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "bubble",
    "header": {
      "type": "box",
      "layout": "horizontal",
      "contents": [
        {
          "type": "text",
          "text": "VIRUS DATABASE",
          "size": "sm",
          "weight": "bold",
          "color": "#AAAAAA"
        }
      ]
    },
    "hero": {
      "type": "image",
      "url": "https://nuuneoi.com/blog/978/coronavirus.jpg",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com/"
      }
    },
    "body": {
      "type": "box",
      "layout": "horizontal",
      "spacing": "md",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "flex": 1,
          "contents": [
            {
              "type": "image",
              "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/02_1_news_thumbnail_1.png",
              "gravity": "bottom",
              "size": "sm",
              "aspectRatio": "4:3",
              "aspectMode": "cover"
            },
            {
              "type": "image",
              "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/02_1_news_thumbnail_2.png",
              "margin": "md",
              "size": "sm",
              "aspectRatio": "4:3",
              "aspectMode": "cover"
            }
          ]
        },
        {
          "type": "box",
          "layout": "vertical",
          "flex": 2,
          "contents": [
            {
              "type": "box",
              "layout": "baseline",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOtMYU1hM0CKc48K8Zbi7F42765qeM4KEiHtwIoD77ZzgqokY-"
                },
                {
                  "type": "text",
                  "text": "เพิ่มข้อมูลไวรัส",
                  "size": "sm",
                  "align": "center",
                  "color": "#006F25",
                  "action": {
                    "type": "message",
                    "label": "1",
                    "text": "1"
                  }
                }
              ]
            },
            {
              "type": "separator",
              "margin": "sm"
            },
            {
              "type": "box",
              "layout": "baseline",
              "margin": "sm",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSL-CCQKpl-BU5Y5CltGCcLhTTTWr-RlY9t8cKNCjKiLPZDBfuk"
                },
                {
                  "type": "text",
                  "text": "ลบข้อมูลไวรัส",
                  "size": "md",
                  "align": "center",
                  "color": "#7E0000",
                  "action": {
                    "type": "message",
                    "label": "2",
                    "text": "2"
                  }
                }
              ]
            },
            {
              "type": "separator",
              "margin": "sm"
            },
            {
              "type": "box",
              "layout": "baseline",
              "margin": "sm",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://image.flaticon.com/icons/svg/457/457710.svg"
                },
                {
                  "type": "text",
                  "text": "อัพเดตข้อมูลไวรัส",
                  "size": "md",
                  "align": "center",
                  "color": "#898900",
                  "action": {
                    "type": "message",
                    "label": "3",
                    "text": "3"
                  }
                }
              ]
            },
            {
              "type": "separator",
              "margin": "sm"
            },
            {
              "type": "box",
              "layout": "baseline",
              "margin": "sm",
              "contents": [
                {
                  "type": "icon",
                  "url": "https://image.flaticon.com/icons/svg/430/430098.svg"
                },
                {
                  "type": "text",
                  "text": "แสดงข้อมูลไวรัส",
                  "size": "md",
                  "align": "center",
                  "color": "#004D6F",
                  "action": {
                    "type": "message",
                    "label": "4",
                    "text": "4"
                  }
                }
              ]
            }
          ]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "horizontal",
      "contents": [
        {
          "type": "button",
          "action": {
            "type": "message",
            "label": "CSV Search",
            "text": "เข้าสู่เมนู CSV Search"
          },
          "color": "#00375F",
          "margin": "xs",
          "height": "sm",
          "style": "primary"
        }
      ]
    }
  }
}
  FLEX_TO_REPLY = Base.get_or_new_from_json_dict(json_data,FlexSendMessage)
  return FLEX_TO_REPLY