from datetime import datetime
import uuid
from .local_qdrant_client import compute_content_hash, is_duplicate, upsert_document

def process_document(text, base_metadata, vector):
    content_hash = compute_content_hash(text)
    if is_duplicate(base_metadata["file_name"], content_hash):
        print(f"[SKIP] Duplicate: {base_metadata['file_name']}")
        return False
    else:
        point_id = str(uuid.uuid4())
        metadata = {
            **base_metadata,
            "content_hash": content_hash,
            "upload_date": datetime.utcnow().isoformat(),
            "document_id": point_id
        }
        upsert_document(vector, metadata)
        print(f"[ADDED] {base_metadata['file_name']}")
        return True
