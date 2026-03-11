import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
chat=client.chats.create(model="gemini-2.5-flash-lite")

initial=True

while True:
    initialPrompt="Scrie ceva la AI:"
    if initial==True:
        print(initialPrompt)
    message=input(">")
    if message=="Exit":
        break;
    res=chat.send_message(message)
    print(res.text)
    initial=False
