# 🎭 Project RAG Muse

## Your Local, Proactive AI Companion with Memory

Muse is a high-performance, memory-driven conversational AI that evolves with you. Built on **RAG (Retrieval-Augmented Generation)** and persistent vector memory, Muse doesn’t just respond—she remembers, adapts, and grows.

## 🧠 Muse doesn’t forget.**

She isn't a static chatbot. By indexing your local files and chat history, she remembers:

- Your past conversations and inside jokes  
- Your active projects and development deadlocks  
- Your personal preferences and daily patterns  

Over time, she transforms from a tool into a true digital companion.

---

# ⚡ Core Features

## 🧠 Persistent Long-Term Memory

Powered by **ChromaDB**, Muse stores and retrieves past interactions using semantic vector search. She recalls context from days or weeks ago to keep conversations fluid.

## 📱 Proactive WhatsApp Bridge

Muse lives on your phone. Using a background thread and **Twilio**, she pings you throughout the day with witty check-ins, progress nudges, or thoughts based on your current project context.

## 👤 Dynamic Identity Discovery

No hardcoding. Muse discovers who you are by reading `knowledge/me.md`.

Change your profile, and her entire perspective and way of addressing you shifts instantly.

## 🔒 Local-First & Private

Runs entirely on your machine via **Ollama**.

- No APIs  
- No Tracking  
- 100% Privacy  
- No data leaves your hardware  

---

# 🚀 Quick Start

## 1️⃣ Clone & Setup

```bash
git clone git@github.com:dev-talib/project-rag-muse.git
cd project-rag-muse

# Setup virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install requirements
pip install chromadb ollama flask twilio python-dotenv
````

## 2️⃣ Configure Environment

Create a `.env` file in the root directory:

```env
TWILIO_SID=your_twilio_sid
TWILIO_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP=whatsapp:+14155238886
TWILIO_MY_NUMBER=whatsapp:+91XXXXXXXXXX
```

## 3️⃣ Personalize Identity

Add your details to `knowledge/me.md`

```markdown
the user's name is mohi.
he is a developer building local intelligence on an ideapad.
```

## 4️⃣ Pull the Brain

```bash
ollama pull gemma3:4b
```

## 5️⃣ Run the Ecosystem

```bash
# Start the AI and Proactive Worker
python main.py

# In a separate terminal start the WhatsApp Webhook
python webhook.py
```

---

# 📂 Project Structure

```plaintext
project-rag-muse/
├── main.py              # CLI Interface + Proactive Worker Thread
├── webhook.py           # Flask Server for WhatsApp Webhooks
├── scripts/
│   ├── engine.py        # RAG Logic, ChromaDB & Persona Management
│   └── utils.py         # SQLite fixes, Twilio Client & Decorators
├── knowledge/           # Your source of truth (me.md, projects.txt)
└── chroma_db/           # Local Vector Storage (Git ignored)
```

---

# 🚧 Roadmap

## ✅ v1.0 — Technical Partner

* RAG system & Persistent memory
* WhatsApp Integration & Proactive Pings
* Dynamic Name Discovery

## 🔜 v2.0 — Companion Mode

* Faster inference & Sentiment-aware responses
* Natural conversation flow (Lower latency)

## 🔜 v2.1 — Multimodal

* Local Voice interaction (TTS/STT)
* Image understanding for shared context

---

# 🧭 Vision

Muse is not just an assistant.

She’s an attempt to build a **second brain** and a **thinking partner** that lives locally and grows with you.

---

# 🧑‍💻 Author

**Mohd Talib (Mohi)**
Building local digital intelligence on an IdeaPad 🚀

```
```
