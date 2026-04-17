import random
from scripts.engine import ChatEngine

def main():
    engine = ChatEngine()
    engine.sync_knowledge()

    greetings = [
        "Ready to build something amazing, Mohi? ✨",
        "Oh! You're back! Found some interesting bits for you. 🧠",
        "Hey partner! Is it time for some magic? 🍬"
    ]
    print(f"\n👓 Pixel: '{random.choice(greetings)}'\n")

    while True:
        user_msg = input("💬 Chat > ").strip()
        if not user_msg: continue
        
        if user_msg.lower() in ["exit", "quit", "q"]:
            print("\n✨ Pixel: 'See you later, Mohi! Happy coding! 👩‍💻'")
            break
            
        if user_msg.lower() == "/clear":
            engine.wipe_memory()
            continue

        try:
            response = engine.chat(user_msg)
            print(f"\n👓 Pixel: {response}\n")
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()