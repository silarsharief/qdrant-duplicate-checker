# Deduplicated PDF Ingestion Pipeline for Qdrant

## Overview
This project provides a pipeline to ingest PDF documents, extract their content and metadata, generate embeddings, and store them in a Qdrant vector database with deduplication based on filename and content hash. It is designed for scalable document ingestion and duplicate detection.

---

## Project Structure

```
.
├── data/
│   ├── set_a/          # New PDFs to ingest
│   └── set_b/          # Sample PDFs to pre-upload for integration test
├── src/
│   ├── pdf_parser.py         # Extract text + metadata using LlamaIndex
│   ├── embedder.py           # Generate embeddings using mixedbread model
│   ├── local_qdrant_client.py# Qdrant setup and helper functions
│   ├── deduplicator.py       # Check for filename + content hash
│   ├── pipeline.py           # Main script to run the pipeline
│   └── __init__.py           # (empty)
├── tests/
│   ├── test_connection.py    # Test Qdrant connection and collection
│   ├── qdsize.py             # Print number of documents in Qdrant collection
│   ├── test_ingestion.py     # Integration test: ingest set_b
│   └── test_ingestion_a.py   # Integration test: ingest set_a
├── requirements.txt          # Python dependencies
├── .env                      # API keys and config (not committed)
├── .gitignore                # Git ignore rules
├── project_structure         # Project structure reference
└── README.md                 # Project documentation
```

---

## Directory and File Explanations

### data/
- **set_a/**: Contains new PDF files to be ingested by the pipeline.
- **set_b/**: Contains sample PDF files for integration testing and pre-upload scenarios.

### src/
- **pdf_parser.py**: Uses LlamaIndex to extract text and metadata (filename, size, extension) from PDF files.
- **embedder.py**: Generates dense vector embeddings for document text using the `mixedbread-ai/mxbai-embed-large-v1` model from Sentence Transformers.
- **local_qdrant_client.py**: Handles Qdrant client setup, collection management, content hashing, duplicate checking, and document upsertion.
- **deduplicator.py**: Checks for duplicates (by filename and content hash) and inserts new documents with metadata and embeddings into Qdrant.
- **pipeline.py**: Main script to run the ingestion pipeline on a folder of PDFs. Handles parsing, embedding, deduplication, and uploading.
- **__init__.py**: Empty file to mark the directory as a Python package.

### tests/
- **test_connection.py**: Script to test connectivity to the Qdrant instance and check for the target collection.
- **qdsize.py**: Prints the number of documents currently stored in the configured Qdrant collection.
- **test_ingestion.py**: Runs the ingestion pipeline on `data/set_b` for integration testing.
- **test_ingestion_a.py**: Runs the ingestion pipeline on `data/set_a` for integration testing.

### Root Files
- **requirements.txt**: Lists all Python dependencies required for the project.
- **.env**: Stores environment variables such as Qdrant URL, API key, and collection name. (Not included in version control.)
- **.gitignore**: Specifies files and folders to be ignored by git, including `.env`, `__pycache__/`, `*.pyc`, `*.log`, and `noneed/`.
- **project_structure**: Reference file describing the intended project layout and file purposes.
- **README.md**: This documentation file.

---

## Setup

1. **Clone the repository**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure environment variables**:
   Create a `.env` file in the root directory with the following variables:
   ```env
   QDRANT_URL=your_qdrant_url
   QDRANT_API_KEY=your_qdrant_api_key
   COLLECTION_NAME=your_collection_name
   ```
4. **Prepare your data**:
   - Place new PDFs in `data/set_a/` or `data/set_b/` as needed.

---

## Usage

- **Ingest PDFs**:
  Run the pipeline on a folder (e.g., `data/set_a`):
  ```bash
  python -m src.pipeline
  ```
  Or use the test scripts in `tests/` for integration testing:
  ```bash
  python tests/test_ingestion.py
  python tests/test_ingestion_a.py
  ```
- **Check Qdrant connection**:
  ```bash
  python tests/test_connection.py
  ```
- **Count documents in Qdrant**:
  ```bash
  python tests/qdsize.py
  ```

---

## Dependencies
- qdrant-client
- sentence-transformers
- llama-index
- PyMuPDF
- python-dotenv
- tqdm

Install all dependencies with `pip install -r requirements.txt`.

---

## Environment Variables
The following variables must be set in your `.env` file:
- `QDRANT_URL`: URL of your Qdrant instance
- `QDRANT_API_KEY`: API key for Qdrant
- `COLLECTION_NAME`: Name of the Qdrant collection to use

---

## Notes
- The `noneed/` folder is ignored and not part of the main pipeline.
- The pipeline skips duplicate documents based on filename and content hash.
- Only PDF files are processed; other file types are ignored.

---

For further details, see comments in the respective source files. 