import os
from tqdm import tqdm
from src.pdf_parser import parse_pdf
from src.embedder import get_embedding
from src.deduplicator import process_document
from src.local_qdrant_client import ensure_collection

def ingest_folder(folder_path: str):
    ensure_collection(vector_size=1024)
    added, skipped = 0, 0

    for file in tqdm(os.listdir(folder_path)):
        if not file.endswith(".pdf"): continue
        path = os.path.join(folder_path, file)

        try:
            text, metadata = parse_pdf(path)
            from datetime import datetime
            metadata["upload_date"] = datetime.now().strftime("%Y-%m-%d")
            vector = get_embedding(text)
            if process_document(text, metadata, vector):
                added += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"[ERROR] Failed to process {file}: {e}")

    print(f"\n✔️ Ingestion complete: {added} added, {skipped} skipped.")
