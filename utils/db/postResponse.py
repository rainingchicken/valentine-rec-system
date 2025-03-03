import pickle
from bson.binary import Binary
from .connectDB import collection


def postResponse(responses, embedding):
    result = collection.insert_one({
        "responses": responses, 
        "embedding": Binary(pickle.dumps(embedding))
        }
    )
    return result.inserted_id
