import os, shutil
from langchain_community.embeddings import LlamaCppEmbeddings
from langchain.schema import Document
from langchain.vectorstores import Chroma

CHROMA_PATH = "./chroma_db"
LLAMA_MODEL_PATH = "/c/Users/prasad/.ollama/models/meta-llama-3.1-8b-instruct-q4_k_m.gguf"  # <-- replace with your local model file

CHROMA_PATH = "chroma"
DATA_PATH = "data"


def main():
    generate_data_store()


def generate_data_store():
    print("Generating data store...")
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)


def load_documents():
    print(f"Loading documents from {DATA_PATH}...")
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents


def split_text(documents: list[Document]):
    print("Splitting documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

    return chunks


def save_to_chroma(chunks: list[Document]):
    # Clear out the database first.
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # Create a LlamaCppEmbeddings instance that points at your local model
    embeddings = LlamaCppEmbeddings(model_path=LLAMA_MODEL_PATH)

    # Create a new Chroma DB from the documents using the local embeddings object.
    db = Chroma.from_documents(
        chunks, embedding=embeddings, persist_directory=CHROMA_PATH
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")


if __name__ == "__main__":
    main()