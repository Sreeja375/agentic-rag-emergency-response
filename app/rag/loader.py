from pathlib import Path
from langchain_community.document_loaders import TextLoader

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"


def load_docs():
    docs = []
    docs.extend(TextLoader(str(DATA_DIR / "first_aid.txt")).load())
    docs.extend(TextLoader(str(DATA_DIR / "emergency_guidelines.txt")).load())
    return docs
