import sys
import os
from qdrant_client import QdrantClient
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.pipeline import ingest_folder

# Load environment variables
load_dotenv()

# Retrieve variables
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)

def get_doc_count():
    return client.count(COLLECTION_NAME).count

if __name__ == "__main__":
    before_count = get_doc_count()
    print(f"Documents before ingestion: {before_count}")
    ingest_folder("data/set_a")
    after_count = get_doc_count()
    print(f"Documents after ingestion: {after_count}")
    print(f"Difference: {after_count - before_count}")
