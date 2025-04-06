class CustomerAgent:
    def __init__(self, embedding_util):
        self.embedding_util = embedding_util

    def get_embedding(self, customer_data):
        return self.embedding_util.generate_embedding(str(customer_data.to_dict()))

