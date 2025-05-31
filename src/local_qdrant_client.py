import hashlib
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)

def ensure_collection(vector_size: int):
    if COLLECTION_NAME not in [c.name for c in client.get_collections().collections]:
        client.create_collection(
            COLLECTION_NAME,
            vectors_config={"text-dense": VectorParams(size=vector_size, distance=Distance.COSINE)}
        )

def compute_content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def is_duplicate(file_name: str, content_hash: str) -> bool:
    hits = client.scroll(
        collection_name=COLLECTION_NAME,
        scroll_filter={
            "must": [
                {"key": "file_name", "match": {"value": file_name}},
                {"key": "content_hash", "match": {"value": content_hash}}
            ]
        },
        limit=1
    )
    return len(hits[0]) > 0

def upsert_document(vector: list, metadata: dict):
    point = PointStruct(
        id=metadata["document_id"],
        vector={"text-dense": vector},
        payload=metadata
    )
    client.upsert(COLLECTION_NAME, [point])
