import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()


API_KEY = os.getenv("GEMINI_API_KEY")  # Or use os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

# Uncomment below to use a model after checking the correct name
model = genai.GenerativeModel('models/gemma-3-27b-it')
chat_history = []
while True:
    prompt = input("You: ")
    if prompt.strip().lower() == "exit":
        print("Exiting chat.")
        break
    chat_history.append(f"User: {prompt}")
    # Combine chat history for context
    context = "\n".join(chat_history)
    response = model.generate_content(context)
    print("Gemini:", response.text)
    chat_history.append(f"Gemini: {response.text}")
