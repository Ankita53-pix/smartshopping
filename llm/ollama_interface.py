import requests

class OllamaClient:
    def __init__(self, model_name="mistral"):
        self.model_name = model_name

    def embed(self, text):
        response = requests.post("http://localhost:11434/api/embeddings",
                                 json={"model": self.model_name, "prompt": text})
        return response.json()["embedding"]

    def chat(self, prompt):
        response = requests.post("http://localhost:11434/api/chat",
                                 json={"model": self.model_name, "prompt": prompt})
        return response.json()["response"]
