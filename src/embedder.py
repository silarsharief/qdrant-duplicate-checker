from sentence_transformers import SentenceTransformer

model = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1")

def get_embedding(text: str) -> list[float]:
    return model.encode(text, normalize_embeddings=True).tolist()
