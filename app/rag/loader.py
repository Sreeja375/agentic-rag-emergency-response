from langchain.document_loaders import TextLoader

def load_docs():
    docs = []
    docs += TextLoader("data/first_aid.txt").load()
    docs += TextLoader("data/emergency_guidelines.txt").load()
    return docs
