import os
import requests

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("Error: Please set the GEMINI_API_KEY environment variable.")
    exit(1)

prompt = input("Enter your prompt: ")

headers = {
    "Content-Type": "application/json"
}
data = {
    "contents": [{"parts": [{"text": prompt}]}]
}
params = {"key": API_KEY}

response = requests.post(GEMINI_API_URL, headers=headers, params=params, json=data)

if response.status_code == 200:
    result = response.json()
    try:
        print("Gemini response:", result["candidates"][0]["content"]["parts"][0]["text"])
    except (KeyError, IndexError):
        print("Unexpected response format:", result)
else:
    print(f"Request failed: {response.status_code}")
    print(response.text)
