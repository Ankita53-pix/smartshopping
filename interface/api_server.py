from fastapi import FastAPI
import pandas as pd
from embeddings.embedding_utils import EmbeddingUtils
from agents.customer_agent import CustomerAgent
from agents.recommender_agent import RecommenderAgent
from agents.data_agent import DataAgent

app = FastAPI()
embedding_util = EmbeddingUtils()
customer_agent = CustomerAgent(embedding_util)
data_agent = DataAgent()
recommender = RecommenderAgent(data_agent)

@app.post("/recommend")
def recommend(customer: dict):
    embedding = customer_agent.get_embedding(pd.Series(customer))
    recs = recommender.recommend(embedding)
    return {"recommendations": recs}