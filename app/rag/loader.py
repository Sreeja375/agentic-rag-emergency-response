from langchain_community.document_loaders import TextLoader


def load_docs():
    docs = []
    docs.extend(TextLoader("data/first_aid.txt").load())
    docs.extend(TextLoader("data/emergency_guidelines.txt").load())
    return docs
