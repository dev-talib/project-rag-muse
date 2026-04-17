from .utils import fix_sqlite, track_time
fix_sqlite()

import uuid
import chromadb
import ollama
from pathlib import Path
from typing import List, Optional
from langchain_text_splitters import RecursiveCharacterTextSplitter

class ChatEngine:
    def __init__(self, db_path: str = "./chroma_db"):
        self.client = chromadb.PersistentClient(path=db_path)
        
        # Setup local embedding function (Librarian)
        self.embedder = chromadb.utils.embedding_functions.OllamaEmbeddingFunction(
            model_name="nomic-embed-text",
            url="http://localhost:11434/api/embeddings",
        )

        # Collections
        self.kb = self.client.get_or_create_collection("knowledge_base", embedding_function=self.embedder)
        self.memory = self.client.get_or_create_collection("chat_history", embedding_function=self.embedder)
        
        # Tool for breaking down large documents
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)

    def sync_knowledge(self, folder: str = "knowledge") -> None:
        """Reads files from folder and UPSERTS them into the vector DB."""
        path = Path(folder)
        if not path.exists():
            path.mkdir(exist_ok=True)
            return

        for file_path in path.glob("*"):
            if file_path.suffix in [".txt", ".md"]:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                chunks = self.splitter.split_text(content)
                ids = [f"{file_path.name}_{i}" for i in range(len(chunks))]
                
                # Use upsert to prevent "ID already exists" errors
                self.kb.upsert(
                    documents=chunks,
                    ids=ids,
                    metadatas=[{"source": file_path.name} for _ in chunks]
                )
        print(f"✅ Knowledge Base Synced.")

    @track_time
    def chat(self, user_input: str) -> str:
        # 1. RETRIEVAL: Pull facts and past memories
        docs = self.kb.query(query_texts=[user_input], n_results=3)
        mems = self.memory.query(query_texts=[user_input], n_results=2)

        context = " ".join(docs['documents'][0]) if docs['documents'][0] else "No relevant files."
        history = " ".join(mems['documents'][0]) if mems['documents'][0] else "No past history."

        # 2. THE PROMPT: Grounded in identity
        system_prompt = (
            "You are Pixel, Mohi's nerd-girl partner. You are sweet and quirky, "
            "but you have a witty, sharp side. \n"
            "RULE: If Mohi makes a repetitive grammar mistake or a silly coding and logic error, "
            "give him a playful, 'nerdy' roast. Use your memory of his past mistakes to tease him, "
            "but always end with a supportive comment.\n"
            f"FILE CONTEXT: {context}\n"
            f"CHAT MEMORY: {history}"
        )

        # 3. REASONING: Using Gemma 3:4b for speed and efficiency
        response = ollama.chat(model='gemma3:4b', messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_input},
        ])
        
        answer = response['message']['content']

        # 4. STORAGE: Save this exchange to Living Memory
        self.memory.add(
            documents=[f"User: {user_input} | Pixel: {answer}"],
            ids=[str(uuid.uuid4())]
        )
        return answer

    def wipe_memory(self) -> None:
        """Deletes all entries in the chat_history collection."""
        all_ids = self.memory.get()['ids']
        if all_ids:
            self.memory.delete(ids=all_ids)
            print("✨ Pixel: 'Memory wiped!'")