import ollama

def getEmbedding(text):
    response = ollama.embed(
    model=text,
    input='Llamas are members of the camelid family',
    )
    embeddings = response["embeddings"]
    return embeddings
