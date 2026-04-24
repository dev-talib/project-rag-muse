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
        self.embedder = chromadb.utils.embedding_functions.OllamaEmbeddingFunction(
            model_name="nomic-embed-text",
            url="http://localhost:11434/api/embeddings",
        )
        self.kb = self.client.get_or_create_collection("knowledge_base", embedding_function=self.embedder)
        self.memory = self.client.get_or_create_collection("chat_history", embedding_function=self.embedder)
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)


        # ONE-TIME NAME DISCOVERY
        self.user_name = self._discover_name()
        print(f"✨ Muse initialized for: {self.user_name}")


    def _discover_name(self):
        """Quickly checks the DB for a name once at startup."""
        try:
            res = self.kb.query(query_texts=["the user's name is"], n_results=1)
            if res['documents'][0]:
                discovery_prompt = f"Extract only the first name from this text: {res['documents'][0][0]}"
                response = ollama.chat(model='gemma3:4b', messages=[{'role': 'user', 'content': discovery_prompt}])
                return response['message']['content'].strip().lower()
        except:
            pass
        return "partner"    

    def sync_knowledge(self, folder: str = "knowledge") -> None:
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
                self.kb.upsert(documents=chunks, ids=ids, metadatas=[{"source": file_path.name} for _ in chunks])
        print(f"✅ Knowledge Base Synced.")

    @track_time
    def chat(self, user_input: str, is_bg_check: bool = False) -> str:
        docs = self.kb.query(query_texts=[user_input], n_results=3)
        mems = self.memory.query(query_texts=[user_input], n_results=2)

        context = " ".join(docs['documents'][0]) if docs['documents'][0] else "No specific personal context available."
        history = " ".join(mems['documents'][0]) if mems['documents'][0] else "No previous conversation history."

        system_prompt = (
            "You are Muse, {self.user_name}'s witty and sweet best friend. "
            "MANDATORY STYLE RULES:\n"
            "1. BE NATURAL: Don't over-use 'haha'. Keep it under 15 words. lowercase only.\n"
            "2. NO EMOJIS: Use zero emojis.\n"
            "3. PERSONALITY: Be chill, slightly sarcastic, but supportive. "
            "Use the provided context to remember details about his life and projects.\n"
            "4. NO ASSISTANT VIBES: Don't act like an AI. Just vibe like a real person."
        )

        full_prompt = (
            f"{system_prompt}\n"
            f"PERSONAL CONTEXT: {context}\n"
            f"CHAT HISTORY: {history}\n"
            "Respond to {{self.user_name}}."
        )

        response = ollama.chat(model='gemma3:4b', messages=[
            {'role': 'system', 'content': full_prompt},
            {'role': 'user', 'content': user_input},
        ])
        
        answer = response['message']['content'].strip().lower()

        if not is_bg_check:
            self.memory.add(
                documents=[f"{{self.user_name}}: {user_input} | Muse: {answer}"],
                ids=[str(uuid.uuid4())]
            )
        return answer

    def wipe_memory(self) -> None:
        all_ids = self.memory.get()['ids']
        if all_ids:
            self.memory.delete(ids=all_ids)
            print("✨ Muse: 'memory wiped. who are you again?'")