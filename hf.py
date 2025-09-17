import requests, os
from dotenv import load_dotenv

load_dotenv()
HF_KEY = os.getenv("HF_API_KEY")
HF_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {HF_KEY}", "accept": "image/png"}

prompt = "a futuristic city skyline at night"
def generate_image(prompt):
    payload = {"inputs": prompt}
    response = requests.post(
        HF_API_URL,
        headers={"Authorization": f"Bearer {HF_KEY}", "accept": "image/png"},
        json=payload,
        timeout=60
    )

    if response.status_code == 200:
        return response.content  # raw image bytes
    else:
        print("HF ERROR:", response.status_code, response.text)
        return None

