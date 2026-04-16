# Pixel 👓✨

**Your Local AI Companion with Memory**

Pixel is a high-performance, memory-driven conversational AI that evolves with you.
Built on **RAG (Retrieval-Augmented Generation)** and persistent vector memory, Pixel doesn’t just respond—she *remembers, adapts, and grows*.

---

## 🧠 Why Pixel?
Pixel doesn’t forget.

She remembers:

* Your past conversations
* Your projects
* Your preferences
* Your patterns

Over time, she transforms from a tool into a **true digital companion**.

---

## ⚡ Core Features

### 🧠 Persistent Long-Term Memory

Powered by ChromaDB, Pixel stores and retrieves past interactions using semantic search.

### 🔎 RAG-Powered Intelligence

Every response is enhanced using relevant memory and knowledge retrieval.

### 📂 Knowledge Base Integration

Drop `.txt` or `.md` files into `/knowledge` and Pixel learns instantly.

### 🔒 Local-First & Private

Runs entirely on your machine via Ollama.
No APIs. No tracking. No data leaving your device.

### 🎭 Personality Engine

Pixel isn’t just functional—she has a personality.
Designed to feel human, not robotic.

---

## 🛠️ Tech Stack

* **Language:** Python 3.11+
* **LLM Runtime:** Ollama
* **Models:** dolphin-mistral, gemma2:2b, phi3:mini
* **Vector DB:** ChromaDB
* **Orchestration:** LangChain (Text Splitters)

---

## 🚀 Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/pixel.git
cd pixel

python -m venv .venv
source .venv/bin/activate

pip install chromadb ollama langchain-text-splitters
```

### Pull Models

```bash
ollama pull gemma2:2b
ollama pull phi3:mini
```

### Run Pixel

```bash
python main.py
```

---

## 📂 Project Structure

```
pixel/
├── main.py              # CLI interface
├── scripts/
│   ├── engine.py        # RAG + memory + persona logic
│   └── utils.py         # performance + fixes
├── knowledge/           # custom knowledge base
└── chroma_db/           # persistent memory
```

---

## 🚧 Roadmap

### ✅ v1.0 — Technical Partner

* RAG system
* Persistent memory
* CLI interface

### 🔜 v2.0 — Companion Mode

* Faster responses
* Emotional intelligence
* Natural conversation flow

### 🔜 v2.1 — Multimodal

* Voice interaction
* Image understanding

---

## 🧭 Vision

Pixel is not just an assistant.

She’s an attempt to build:

* A second brain
* A thinking partner
* A system that grows with you

---

## 🧑‍💻 Author

**Mohi (Mohd Talib)**
Building local digital intelligence on an IdeaPad 🚀
