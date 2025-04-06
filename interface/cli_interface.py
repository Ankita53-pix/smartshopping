import pandas as pd
from embeddings.embedding_utils import EmbeddingUtils
from agents.customer_agent import CustomerAgent
from agents.product_agent import ProductAgent
from agents.recommender_agent import RecommenderAgent
from agents.data_agent import DataAgent

customer_df = pd.read_csv("customer_data_collection.csv")
product_df = pd.read_csv("product_recommendation_data.csv")

embedding_util = EmbeddingUtils()
customer_agent = CustomerAgent(embedding_util)
data_agent = DataAgent()
product_agent = ProductAgent(embedding_util, data_agent)
recommender = RecommenderAgent(data_agent)

product_agent.index_products(product_df)
customer = customer_df.iloc[0]
embedding = customer_agent.get_embedding(customer)
recommendations = recommender.recommend(embedding)
print("\nTop Recommendations:")
for r in recommendations:
    print(r)

