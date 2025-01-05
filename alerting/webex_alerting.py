
import requests

WEBEX_API_URL = "https://webexapis.com/v1/messages"

def send_webex_alert(WEBEX_BOT_TOKEN,ROOM_ID,messages):
    headers = {
         "Authorization": f"Bearer {WEBEX_BOT_TOKEN}",
         "Content-Type": "application/json"
    }
    data = {
        "roomId": ROOM_ID,
        "text": messages
    }
    response = requests.post(WEBEX_API_URL,headers=headers,json=data)

    if response.status_code == 200:
        print("Alert sent successfully!")
    else:
        print(f"Failed to send alert. Status code: {response.status_code}")
        print(response.json())

if __name__ == '__main__':
    messages = "Hello world, testing webex alert"
    send_webex_alert("WEBEX_BOT_TOKEN","ROOM_ID",messages)