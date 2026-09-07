import chromadb
from sentence_transformers import SentenceTransformer

# Our chunks
chunks = [
    "RAG retrieves relevant information from documents.",
    "Embeddings represent the meaning of text.",
    "Football is played between two teams."
]

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create Chroma client
client = chromadb.PersistentClient(path="./chroma_db")

# Create a collection
collection = client.get_or_create_collection(
    name="rag_documents"
)

# Create embeddings
embeddings = model.encode(chunks).tolist()

# Store chunks + embeddings
collection.add(
    ids=["chunk_1", "chunk_2", "chunk_3"],
    documents=chunks,
    embeddings=embeddings
)

print("Chunks stored successfully!")