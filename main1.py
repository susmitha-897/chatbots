import requests

try:
    r = requests.get("https://chat.deepseek.com/")
    print("Connected! Status code:", r.status_code)
except Exception as e:
    print("Error:", e)
