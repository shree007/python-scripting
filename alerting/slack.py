import requests
import json

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/XXX/YYY/ZZZ"

def send_slack_alert(message):
    payload = {"text": message}
    headers = {"Content-Type": "application/json"}
    response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        print("✅ Slack alert sent successfully!")
    else:
        print(f"❌ Failed to send alert: {response.status_code}, {response.text}")


if __name__ == '__main__':
    send_slack_alert("🚀 Alert: Something happened!")
