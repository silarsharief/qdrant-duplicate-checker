from llama_index.readers.file import PDFReader
import os

def parse_pdf(filepath):
    reader = PDFReader()
    docs = reader.load_data(filepath)
    text = "\n".join(doc.text for doc in docs)
    file_size = os.path.getsize(filepath)
    file_name = os.path.basename(filepath)
    return text, {
        "file_name": file_name,
        "file_size": file_size,
        "extension": ".pdf"
    }
