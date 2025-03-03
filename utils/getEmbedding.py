import ollama

def getEmbedding(text):
    response = ollama.embeddings(model='nomic-embed-text', prompt=text)
    embeddings = response["embedding"]
    return embeddings
