import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API Key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

print("🤖 Gemini Chatbot Ready! Type 'quit' to exit.\n")

# Keep conversation history
chat = model.start_chat(history=[])

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("👋 Goodbye!")
        break

    response = model.generate_content(user_input)
    print("Gemini:", response.text)
        