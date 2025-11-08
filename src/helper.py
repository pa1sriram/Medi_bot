from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
from langchain_core.documents import Document
from langchain_huggingface.embeddings import HuggingFaceEmbeddings


def load_pdf_files(data):
    loader = DirectoryLoader(data, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents


def filter_to_minimize_docs(docs: List[Document]) -> List[Document]:
    """
    Gives a list of document objects, return a new list of document objects
    containing only 'source' in metadata and the original page_content
    """
    minimal_doc: List[Document] = []
    for doc in docs:
        src = doc.metadata.get("source")
        minimal_doc.append(
            Document(
                page_content = doc.page_content,
                metadata = {"source": src}
            )
        )
    return minimal_doc


#Split the documents into smaller chunks
def text_split(min_doc):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=200,
    )
    text_chunk = text_splitter.split_documents(min_doc)
    return text_chunk


# from langchain.embeddings import HuggingFaceEmbeddings
def download_embeddings():
    """
    Download and return the HuggingFace embedding model.
    """
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
    )
    return embeddings

embedding = download_embeddings()