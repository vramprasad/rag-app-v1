from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
import os

DATA_DIR = "../data"
DB_DIR = "../db"

# Load PDFs
documents = []
for file in os.listdir(DATA_DIR):
    if file.endswith(".pdf"):
        print(f"Processing {file}...")
        loader = PyPDFLoader(os.path.join(DATA_DIR, file))
        documents.extend(loader.load())

# Split text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = text_splitter.split_documents(documents)

# Embeddings (local via Ollama)
embeddings = OllamaEmbeddings(model="myllama3")

# Store in Chroma
vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=DB_DIR
)

vectordb.persist()

print("✅ Ingestion complete. Vector DB created.")
