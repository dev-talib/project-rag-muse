import os
import threading
from flask import Flask, request
from twilio.rest import Client
from scripts.engine import ChatEngine
from dotenv import load_dotenv

load_dotenv()
account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_TOKEN')
whatsapp_from = os.getenv('TWILIO_WHATSAPP')

app = Flask(__name__)
engine = ChatEngine()
client = Client(account_sid, auth_token)

def process_and_reply(user_msg, sender_number):
    try:
        muse_answer = engine.chat(user_msg, is_bg_check=False)
        client.messages.create(from_=whatsapp_from, body=muse_answer, to=sender_number)
        print(f"✅ Reply sent to {sender_number}")
    except Exception as e:
        print(f"❌ Error: {e}")

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    user_msg = request.values.get('Body', '').strip()
    sender = request.values.get('From', '')

    if user_msg.lower() == "muse, reset":
        engine.wipe_memory()
        client.messages.create(from_=whatsapp_from, body="memory wiped. who are you?", to=sender)
        return '', 200

    threading.Thread(target=process_and_reply, args=(user_msg, sender)).start()
    return '', 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)