from sklearn.metrics.pairwise import cosine_similarity
from db.connectDB import client
import pickle

def getMatch(current_user_id, current_embedding):
    all_responses = list(client.collection.find())
    similarities = []
    for doc in all_responses:
        if doc['_id'] == current_user_id:
            continue
        stored_embedding = pickle.loads(doc['embeddings'])
        similarity = cosine_similarity(['current_embedding'], [stored_embedding])[0][0]
        similarities.append((similarity, doc['responses']))
    similarities.sort(reverse=True, key=lambda x:x[0])
    return similarities[0][1] if similarities else None