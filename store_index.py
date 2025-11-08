from dotenv import load_dotenv
import os
from pinecone import ServerlessSpec
from pinecone import Pinecone
from src.helper import text_split, download_embeddings, load_pdf_files, filter_to_minimize_docs
from langchain_pinecone import Pinecone as PineconeFromDocs


load_dotenv()

# It's recommended to set your API key as an environment variable
PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
Gemini_API_KEY = os.getenv("GeminiAI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GOOGLE_API_KEY"] = Gemini_API_KEY

extracted_data = load_pdf_files("data")
min_doc = filter_to_minimize_docs(extracted_data)
text_chunks = text_split(min_doc)
HuggingFaceembedding = download_embeddings()

pinecone_api_key = PINECONE_API_KEY
index_name = "medical-chatbot"
pc = Pinecone(api_key= pinecone_api_key)



if index_name not in pc.list_indexes().names():
    pc.create_index(
        name = index_name,
        dimension = 384,
        metric = "cosine",
        spec = ServerlessSpec(cloud = "aws", region = "us-east-1")
    )
index = pc.Index(index_name)




# The rest of your code that prepares text_chunks, embedding, and index_name
# ...
docsearch = PineconeFromDocs.from_documents(
    documents=text_chunks,
    embedding=HuggingFaceembedding,
    index_name=index_name,
)

# Load existing index
#Embed each chunk and upsert the embeddings into your pinecone index
docsearch = PineconeFromDocs.from_existing_index(
    index_name = index_name,
    embedding = HuggingFaceembedding
)