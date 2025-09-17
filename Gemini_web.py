import os
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

# Load API Key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Create Flask app
app = Flask(__name__)

# Chat session (so conversation remembers history)
chat = model.start_chat(history=[])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_with_gemini():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"reply": "❌ Please type something!"}), 400


    response = chat.send_message(user_message)
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(debug=True)
