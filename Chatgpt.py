import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_KEY:
    raise RuntimeError("❌ OPENAI_API_KEY not found in .env file")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_KEY)

print("🤖 ChatGPT Chatbot Ready! Type 'quit' to exit.")

# Conversation loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break

    try:
        # Send user input to ChatGPT
        response = client.chat.completions.create(
            model="gpt-4o-mini",   # Fast + cheap, you can use "gpt-4o" too
            messages=[
                {"role": "system", "content": "You are a helpful AI chatbot."},
                {"role": "user", "content": user_input}
            ]
        )

        # Print assistant reply
        print("ChatGPT:", response.choices[0].message.content)

    except Exception as e:
        print("❌ Error:", e)
