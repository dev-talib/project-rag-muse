import sys
import time
import os
from typing import Callable, Any
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables for Twilio
load_dotenv()

def fix_sqlite() -> None:
    """Redirects sqlite3 to pysqlite3 for Ubuntu 20.04 compatibility."""
    try:
        __import__('pysqlite3')
        sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
    except ImportError:
        pass

def track_time(func: Callable) -> Callable:
    """Decorator to measure how long the AI takes to think."""
    def wrapper(*args, **kwargs) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"⏱️  (Thought for {end - start:.2f} seconds)")
        return result
    return wrapper

def send_whatsapp(message_body: str) -> None:
    """Sends a WhatsApp message via Twilio using credentials from .env."""
    try:
        account_sid = os.getenv('TWILIO_SID')
        auth_token = os.getenv('TWILIO_TOKEN')
        whatsapp_from = os.getenv('TWILIO_WHATSAPP')
        # This is the number where you want to receive proactive pings
        whatsapp_to = os.getenv('TWILIO_MY_NUMBER') 

        if not all([account_sid, auth_token, whatsapp_from, whatsapp_to]):
            print("Error: Twilio credentials or phone numbers missing in .env")
            return

        client = Client(account_sid, auth_token)
        client.messages.create(
            from_=whatsapp_from,
            body=message_body,
            to=whatsapp_to
        )
        print(f"📲 WhatsApp message sent.")
    except Exception as e:
        print(f"Failed to send WhatsApp: {e}")