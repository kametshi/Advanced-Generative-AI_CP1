# rag.py

from sentence_transformers import SentenceTransformer
import chromadb
from pathlib import Path

# ---------------- CONFIG ----------------

BASE_DIR = Path(__file__).parent
DB_DIR = BASE_DIR / "db" / "chroma"

COLLECTION_NAME = "support_docs"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# 👉 порог качества (чем МЕНЬШЕ — тем строже)
MAX_DISTANCE = 0.9

# 👉 допустимая доля мусорных символов
MAX_GARBAGE_RATIO = 0.1

# ---------------- INIT ----------------

_embedder = SentenceTransformer(MODEL_NAME)
_client = chromadb.PersistentClient(path=str(DB_DIR))
_collection = _client.get_or_create_collection(name=COLLECTION_NAME)

print("CHROMA COUNT:", _collection.count())

# ---------------- HELPERS ----------------

def is_garbage(text: str) -> bool:
    """
    Проверка OCR-мусора (����� и т.п.)
    """
    if not text:
        return True

    bad_chars = text.count("�")
    ratio = bad_chars / max(len(text), 1)

    return ratio > MAX_GARBAGE_RATIO


# ---------------- MAIN API ----------------

def retrieve(query: str, top_k: int = 4):
    """
    Возвращает только КАЧЕСТВЕННЫЕ результаты.
    Если ничего не найдено — вернёт [].
    """

    # embedding запроса
    q_vec = _embedder.encode([query]).tolist()[0]

    # запрос в Chroma
    res = _collection.query(
        query_embeddings=[q_vec],
        n_results=top_k,
        include=["documents", "metadatas", "distances"]
    )

    # защита от пустого ответа
    if not res["documents"] or not res["documents"][0]:
        return []

    docs = res["documents"][0]
    metas = res["metadatas"][0]
    dists = res["distances"][0]

    items = []

    for doc, meta, dist in zip(docs, metas, dists):

        # 1️⃣ слишком далеко по смыслу
        if dist > MAX_DISTANCE:
            continue

        # 2️⃣ OCR-мусор
        if is_garbage(doc):
            continue

        items.append({
            "text": doc,
            "source": meta.get("source", "unknown"),
            "page": meta.get("page", "?"),
            "distance": dist
        })

    return items
