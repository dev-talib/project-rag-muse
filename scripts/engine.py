from scripts.utils import fix_sqlite, track_time
fix_sqlite()

import uuid
import chromadb
import ollama
from pathlib import Path
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter

class ChatEngine:
    def __init__(self, db_path="./chroma_db"):
        self.client = chromadb.PersistentClient(path=db_path)
        self.kb = self.client.get_or_create_collection(name="knowledge_base")
        self.memory = self.client.get_or_create_collection(name="chat_history")
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

    def ingest_docs(self, folder="knowledge"):
        path = Path(folder)
        if not path.exists():
            os.makedirs(folder, exist_ok=True)
            return

        for file in path.glob("*"):
            if file.suffix in [".txt", ".md"]:
                with open(file, "r", encoding="utf-8") as f:
                    content = f.read()
                chunks = self.splitter.split_text(content)
                ids = [f"{file.name}_{i}" for i in range(len(chunks))]
                self.kb.add(documents=chunks, ids=ids, metadatas=[{"source": file.name} for _ in chunks])

    def clear_all_memory(self):
        results = self.memory.get()
        if results['ids']:
            self.memory.delete(ids=results['ids'])
            print("\n✨ Pixel: 'Memory wiped!'")

    @track_time
    def chat(self, user_input):
        doc_results = self.kb.query(query_texts=[user_input], n_results=3)
        mem_results = self.memory.query(query_texts=[user_input], n_results=2)
        context = " ".join(doc_results['documents'][0]) if doc_results['documents'] else "none"
        history = " ".join(mem_results['documents'][0]) if mem_results['documents'] else "start"

        system_identity = "You are Pixel, Mohi's nerd-girl partner. Be sweet and quirky."
        prompt = f"{system_identity}\nHistory: {history}\nContext: {context}\nUser: {user_input}"

        response = ollama.generate(model="dolphin-mistral", prompt=prompt)
        answer = response['response']
        self.memory.add(documents=[f"M: {user_input} | P: {answer}"], ids=[str(uuid.uuid4())])
        return answer
