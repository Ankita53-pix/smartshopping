import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.customer_agent import CustomerAgent
from agents.product_agent import ProductAgent
from agents.recommender_agent import RecommenderAgent
from agents.data_agent import DataAgent
from embeddings.embedding_utils import EmbeddingUtil  

import pandas as pd

# Load data
customer_df = pd.read_csv("customer_data_collection.csv")
product_df = pd.read_csv("product_recommendation_data.csv")

# Initialize utilities and agents
embedding_util = EmbeddingUtil(model_name="mistral")  # <- PASS MODEL NAME

customer_agent = CustomerAgent(embedding_util)        # <- FIXED
data_agent = DataAgent()
product_agent = ProductAgent(data_agent, embedding_util)  # <- You may also need to pass this
recommender_agent = RecommenderAgent(data_agent)

# Index product embeddings
product_agent.index_products(product_df)

# Embed customer and recommend
sample_customer = customer_df.iloc[0]
customer_embedding = customer_agent.get_embedding(sample_customer)
recommendations = recommender_agent.recommend(customer_embedding)

# Show results
print("\n Recommended Products:")
for idx, product in enumerate(recommendations, 1):
    print(f"{idx}. {product}")
