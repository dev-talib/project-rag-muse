import os
import sys
import random

# Force Python to look in the current directory for the 'scripts' folder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from scripts.utils import fix_sqlite

# Run the sqlite fix before anything else
fix_sqlite()

try:
    from scripts.engine import ChatEngine
except ImportError as e:
    print(f"❌ Critical Import Error: {e}")
    # This helps us see where Python is actually looking
    print(f"DEBUG: Python Path is: {sys.path}")
    sys.exit(1)

def main():
    engine = ChatEngine()
    
    print("⚡ Syncing Knowledge Base...")
    engine.ingest_docs()
    
    greetings = [
        "Ready to build something amazing today, Mohi? ✨",
        "I've been organizing our memory files all morning! What's the plan? 👩‍💻",
        "Oh! You're back! I found some super interesting bits for you. 🧠",
        "Hey partner! Is it time to make some magic happen? 🍬"
    ]

    print(f"\n👓 Pixel: '{random.choice(greetings)}'\n")

    while True:
        try:
            user_msg = input("💬 Chat > ").strip()
            if not user_msg: continue
            if user_msg.lower() in ["exit", "quit", "q"]:
                print("\n✨ Pixel: 'Wait, you're leaving? Okay, see you later, Mohi! Happy coding! 👩‍💻' *waves*")
                break
            if user_msg.lower() == "/clear":
                engine.clear_all_memory()
                continue

            response = engine.chat(user_msg)
            print(f"\n👓 Pixel: {response}\n")

        except KeyboardInterrupt:
            print("\n\n✨ Pixel: 'Keyboard interrupt! Catch you later, Mohi! 🏃‍♀️'")
            break
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()