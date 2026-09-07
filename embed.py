from sentence_transformers import SentenceTransformer

chunks = [
    "RAG retrieves relevant information from documents.",
    "Embeddings represent the meaning of text.",
    "Football is played between two teams."
]

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(chunks)

for i, embedding in enumerate(embeddings):
    print(f"\n===== CHUNK {i + 1} =====")
    print(embedding)