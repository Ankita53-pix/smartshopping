from llm.ollama_interface import OllamaClient

class EmbeddingUtil:
    def __init__(self):
        self.client = OllamaClient()

    def generate_embedding(self, text):
        return self.client.embed(text)
