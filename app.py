from flask import Flask, render_template, jsonify, request
from src.helper import download_embeddings
# from langchain_pinecone import PineconeVectorStore
from langchain_pinecone import Pinecone
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os


app=Flask(__name__)

load_dotenv()

PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
Gemini_API_KEY = os.getenv("GeminiAI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GOOGLE_API_KEY"] = Gemini_API_KEY

embedding = download_embeddings()

index_name = "medical-chatbot"

docsearch = Pinecone.from_existing_index(
    index_name = index_name,
    embedding = embedding
)

retriver = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})
chatModel = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
prompt = ChatPromptTemplate.from_messages(
    [  
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriver, question_answer_chain)

@app.route("/")
def index():
    return render_template("chat.html")

#route for handling user queries like when ever user send his quarry through the chat interface
@app.route("/get", methods=["Get", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input": msg})
    print("Response : ", response["answer"])
    return str(response["answer"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 8080, debug= True)