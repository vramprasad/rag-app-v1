from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough



# Load vector DB
embeddings = OllamaEmbeddings(model="myllama3")
vectordb = Chroma(
    persist_directory="../db",
    embedding_function=embeddings
)

retriever = vectordb.as_retriever(search_kwargs={"k": 3})

# Local LLM
llm = Ollama(model="myllama3")

# Prompt
prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant.
Answer the question ONLY using the context below.
If the answer is not present, say "I don't know".

Context:
{context}

Question:
{question}
""")

# RAG Chain (LCEL)
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
)

# Interactive loop
while True:
    q = input("\nAsk a question (or exit): ")
    if q.lower() == "exit":
        break
    print("\nAnswer:\n", rag_chain.invoke(q))
