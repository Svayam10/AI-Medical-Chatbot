from langchain_community.document_loaders import pyPDFLoader , DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Step 1: Load Raw PDFs
DATA_PATH = "data/"

def load_pdf_files():
    loader = DirectoryLoader(data, glob="*.pdf", loader_cls=pyPDFLoader)
    documents = loader.load()
    return documents
# Step 2: Create Chunks
# Step 3: Create Vector Embeddings
# Step 4: Create Vector Store in FAISS