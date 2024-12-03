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

@app.get("/")
async def health_check():
    return "Ready to go cap"
