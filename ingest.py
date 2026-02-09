from pathlib import Path
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
import os

DOCS_DIR = Path("data/docs")
DB_DIR = "data/chroma"

os.makedirs(DB_DIR, exist_ok=True)

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def get_client():
    return chromadb.PersistentClient(path=DB_DIR)


def get_collection():
    client = get_client()
    return client.get_or_create_collection(name="rag_docs")


def ingest_pdf(pdf_path, progress_callback=None):
    collection = get_collection()
    reader = PdfReader(pdf_path)

    total = 0

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if not text:
            continue

        embedding = model.encode(text).tolist()

        collection.add(
            documents=[text],
            embeddings=[embedding],
            metadatas=[{
                "source": pdf_path.name,
                "page": i + 1
            }],
            ids=[f"{pdf_path.name}_{i}"]
        )

        total += 1

        if progress_callback:
            progress_callback(f"{pdf_path.name} page {i+1}")

    return total


def ingest_all_pdfs(progress_callback=None):
    total_chunks = 0
    print("DOCS_DIR:", DOCS_DIR)
    print("Files:", list(DOCS_DIR.glob("*")))
    pdf_files = list(DOCS_DIR.glob("*.pdf"))

    if not pdf_files:
        return 0

    for pdf in pdf_files:
        total_chunks += ingest_pdf(pdf, progress_callback)

    return total_chunks


def chroma_count():
    collection = get_collection()
    return collection.count()
