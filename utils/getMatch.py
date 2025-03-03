from sklearn.metrics.pairwise import cosine_similarity
from .db.connectDB import collection
import pickle
import numpy as np

def getMatch(current_embedding, current_user_id):
    all_responses = list(collection.find())
    similarities = []

    for doc in all_responses:
        if doc["_id"] == current_user_id:
            continue

        stored_embedding = pickle.loads(doc["embedding"])
        similarity = cosine_similarity([current_embedding], [stored_embedding])[0][0]
        similarities.append((similarity, doc["responses"]))
   
    similarities.sort(reverse=True, key=lambda x: x[0])
    return similarities if similarities else None
