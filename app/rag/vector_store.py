from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from .loader import load_docs


def build_vector_store():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    docs = load_docs()
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore
