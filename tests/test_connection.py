import os
from qdrant_client import QdrantClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve variables
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# Test connection to Qdrant
def test_qdrant_connection():
    try:
        client = QdrantClient(
            url=QDRANT_URL,
            api_key=QDRANT_API_KEY,
        )
        
        # List collections to check if connection works
        collections = client.get_collections()
        print("✅ Qdrant connection successful.")
        print("Available collections:", [col.name for col in collections.collections])
        
        if COLLECTION_NAME in [col.name for col in collections.collections]:
            print(f"✅ Target collection '{COLLECTION_NAME}' exists.")
        else:
            print(f"⚠️ Collection '{COLLECTION_NAME}' not found.")
    
    except Exception as e:
        print("❌ Failed to connect to Qdrant.")
        print("Error:", e)

if __name__ == "__main__":
    test_qdrant_connection()
