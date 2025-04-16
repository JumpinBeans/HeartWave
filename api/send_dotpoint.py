# ~/KairoVault/api/send_dotpoint.py

import requests
import json
import sys

# Replace this with your Pi’s local IP if needed
API_URL = "http://192.168.20.40:5000/dotpoint"

def send_dotpoint(label, intent, emotion, outcome=None):
    payload = {
        "label": label,
        "intent": intent,
        "emotion": emotion,
        "outcome": outcome or ""
    }

    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            print("✅ Dotpoint recorded successfully.")
        elif response.status_code == 202:
            print("⚠️ Dotpoint received, but reflection may be needed:")
            print(response.json())
        else:
            print("❌ Failed to log dotpoint:", response.status_code, response.text)
    except Exception as e:
        print("❌ Error connecting to vault:", str(e))

# Example use — replace with any values or call from another script
if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 send_dotpoint.py 'Label' 'Intent' 'Emotion' ['Outcome']")
    else:
        label = sys.argv[1]
        intent = sys.argv[2]
        emotion = sys.argv[3]
        outcome = sys.argv[4] if len(sys.argv) > 4 else None
        send_dotpoint(label, intent, emotion, outcome)
