#תיעוד לשרת
import requests

# בעת בקשת GET

#(param) :
headers = {
    "machine": "RCX1234", #אם הוא ירצה לבחור סוג מחשב

    #מידע חובה :
    "t_security": " [85, 92, 78, 90] " , # אבטחת טוקן
    "X-Source-URL": "https://example.com/original-page" # URL
}

response = requests.post("https://yourserver.com/receive-data", headers=headers)

#בקשת POST

#URL :
url = 'https://www.aaa.com/וכו'
#(param) :
data = {'machine': '000' , #חובה
        'date_time': 'תבנית שעה' , #אם רלוונטי
        'data': 'מינגכלחגק' , # אם רלוונטי

    #מידע חובה :
    "t_security": " [85, 92, 78, 90] " , # אבטחת טוקן
    "X-Source-URL": "https://example.com/original-page" # URL
    }

x = requests.post(url, json = data)

print(x.text)

# בנוסף מומש מתודה בסיסית בלבד של PUT and DELETE