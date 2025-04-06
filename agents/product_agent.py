class ProductAgent:
    def __init__(self, embedding_util, data_agent):
        self.embedding_util = embedding_util
        self.data_agent = data_agent

    def index_products(self, product_df):
        for _, row in product_df.iterrows():
            embedding = self.embedding_util.generate_embedding(str(row.to_dict()))
            self.data_agent.insert_product(row.to_dict(), embedding)


