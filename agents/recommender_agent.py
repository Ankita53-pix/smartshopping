from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class RecommenderAgent:
    def __init__(self, data_agent):
        self.data_agent = data_agent

    def recommend(self, customer_embedding, top_k=5):
        products = self.data_agent.get_all_product_embeddings()
        product_ids = [p[0] for p in products]
        product_embeddings = [p[1] for p in products]
        similarities = cosine_similarity([customer_embedding], product_embeddings)[0]
        ranked = np.argsort(similarities)[::-1][:top_k]
        return [product_ids[i] for i in ranked]
    

