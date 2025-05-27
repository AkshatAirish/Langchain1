from langchain.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = "Hello world"
embedding_vector = embedding.embed_query(text)
print(embedding_vector[:5])  # Print first 5 values
