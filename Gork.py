import os
import requests
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_KEY = os.getenv("GROK_API_KEY")

if not API_KEY:
    raise RuntimeError("❌ GROK_API_KEY not found in .env file")

# Grok API endpoint
url = "https://api.x.ai/v1/chat/completions"

print("🤖 Grok Chatbot Ready! Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break

    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {
        "model": "grok-beta",   # model name may vary (check docs)
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        bot_reply = data["choices"][0]["message"]["content"]
        print("Grok:", bot_reply)
    else:
        print("❌ Error:", response.text)
