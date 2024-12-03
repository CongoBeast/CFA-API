from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.schema import Document
# from langchain.llms import ChatOpenAI
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from PyPDF2 import PdfReader
import os
from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the request schema
class ChatRequest(BaseModel):
    user_message: str
    chat_history: list[dict] = []  # Optional: A list of previous messages between the user and bot

@app.post("/chat")
async def chat(request: ChatRequest):
    """
    Chatbot endpoint to process user messages and respond.
    """
    try:
        # Prepare the messages for the GPT model
        messages = request.chat_history + [
            {"role": "user", "content": request.user_message}
        ]
        # OpenAI completion request
        response = openai.ChatCompletion.create(
            model="gpt-4",  # You can use "gpt-3.5-turbo" for cost-effective options
            messages=messages,
            max_tokens=150
        )
        bot_message = response["choices"][0]["message"]["content"].strip()

        # Return the chatbot's response
        return {
            "bot_message": bot_message,
            "chat_history": messages + [{"role": "assistant", "content": bot_message}]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def health_check():
    return "Ready to go cap"
