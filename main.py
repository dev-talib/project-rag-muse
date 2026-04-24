import random
import threading
import time
from datetime import datetime
from scripts.engine import ChatEngine
from scripts.utils import send_whatsapp

def autonomous_worker(engine: ChatEngine):
    """Pings user like a real friend during the day based on personal context."""
    name = engine.user_name
    while True:
        # Check in every 1.5 to 3 hours
        time.sleep(random.randint(5400, 10800)) 
        
        now = datetime.now()
        if 8 <= now.hour < 22:
            # Generic proactive instruction
            instruction = (
                "check your knowledge base for any recent notes or plans. "
                "send a short, witty text to {name} checking in or teasing him "
                "about his current progress."
            )
            nudge = engine.chat(instruction, is_bg_check=True)
            send_whatsapp(nudge)
            print(f"☀️ Daytime ping sent: {nudge}")
        else:
            print(f"🌙 Night mode: Muse is quiet.")

def main():
    engine = ChatEngine()
    engine.sync_knowledge()

    bg_thread = threading.Thread(target=autonomous_worker, args=(engine,), daemon=True)
    bg_thread.start()

    greetings = [
        "Ready to build something amazing? ✨",
        "The Muse is awake. What's the plan? 🧠",
        "Hey partner! Ready to create some magic? 🍬"
    ]
    print(f"\n👓 Project RAG Muse: '{random.choice(greetings)}'\n")
    print("🚀 Proactive Worker is running in the background...")

    while True:
        try:
            user_msg = input("💬 Chat > ").strip()
            if not user_msg: continue
            if user_msg.lower() in ["exit", "quit", "q"]: break
            if user_msg.lower() == "/clear":
                engine.wipe_memory()
                continue
            print(f"\n👓 Muse: {engine.chat(user_msg)}\n")
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == "__main__":
    main()