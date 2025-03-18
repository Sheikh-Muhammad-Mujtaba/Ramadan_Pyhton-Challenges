import google.generativeai as genai
from dotenv import load_dotenv
import os
import chainlit as cl


load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])


model = genai.GenerativeModel(model_name="gemini-2.0-flash")


@cl.on_chat_start
async def handle_chat_start():
    await cl.Message(content=f"**Assalamualikum**, \nHow can I help you Today?😊").send()


@cl.on_message
async def main(message: cl.Message):
    prompt = message.content
    response = model.generate_content(prompt)

    response_text = response.text if hasattr(response, "text") else ""
    await cl.Message(content=response_text).send()
