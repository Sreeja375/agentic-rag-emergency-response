from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from .loader import load_docs


def build_vector_store():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    docs = load_docs()
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore
