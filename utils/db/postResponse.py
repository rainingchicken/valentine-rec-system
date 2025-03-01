import pickle
from bson.binary import Binary
from connectDB import client

def postResponse(responses, embedding):
    result = client.collection.insert_one({
        "responses": responses,
        "embedding": Binary(pickle.dumps(embedding))  # Store embeddings as binary
    })
    return result.inserted_id 