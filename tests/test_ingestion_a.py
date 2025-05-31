import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.pipeline import ingest_folder

if __name__ == "__main__":
    ingest_folder("data/set_a")
