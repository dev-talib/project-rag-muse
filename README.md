# 🎭 project-rag-muse

**Your Local AI Companion with Memory**

Muse is a high-performance, memory-driven conversational AI that evolves with you.  
Built on **RAG (Retrieval-Augmented Generation)** and persistent vector memory, Muse doesn’t just respond—she *remembers, adapts, and grows*.

---

## 🧠 Muse doesn’t forget.
She remembers:

- Your past conversations  
- Your projects  
- Your preferences  
- Your patterns  

Over time, she transforms from a tool into a **true digital companion**.

---

## ⚡ Core Features

### 🧠 Persistent Long-Term Memory
Powered by ChromaDB, Muse stores and retrieves past interactions using semantic search.

### 🔎 RAG-Powered Intelligence
Every response is enhanced using relevant memory and contextual retrieval.

### 📂 Knowledge Base Integration
Drop `.txt` or `.md` files into `/knowledge` and Muse learns instantly.

### 🔒 Local-First & Private
Runs entirely on your machine via Ollama.  
No APIs. No tracking. No data leaving your device.

### 🎭 Personality Engine
Muse isn’t just functional—she has a personality.  
Designed to feel human, adaptive, and conversational.

---
## 🚀 Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/pixel.git
cd pixel

uv venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

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
  
---

## 🧭 Vision

muse is not just an assistant.

She’s an attempt to build:

* A second brain
* A thinking partner
* A system that grows with you

---

## 🧑‍💻 Author

**Mohd Talib (Mohi)**
Building local digital intelligence on an IdeaPad 🚀
