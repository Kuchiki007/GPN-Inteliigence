import requests

class ChatModel:
    def __init__(self):
        self.model = "http://localhost:11434/api/chat"

    def __call__(self, user_input, context):
        payload = {
            "model": "mistral",
            "messages": context,
            "stream": False
        }
        response = requests.post(self.model, json=payload)
        response.raise_for_status()
        data = response.json()
        reply = data["message"]["content"]
        return reply