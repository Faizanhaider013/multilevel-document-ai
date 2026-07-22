import os

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter

# -----------------------------
# Embedding Model
# -----------------------------
embedding_function = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------
# Split Documents
# -----------------------------
def split_text(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=150,
    )

    chunks = splitter.split_documents(documents)

    print(f"✂️ Created {len(chunks)} chunks")
    return chunks


# -----------------------------
# Create Vector Store
# -----------------------------
def create_vector_store(chunks):
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_function,
        persist_directory="./chroma_db",
        collection_name="rag_docs",
    )

    print("✅ Vector Store Created")
    return vector_store


# -----------------------------
# Format Retrieved Documents
# -----------------------------
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


# -----------------------------
# RAG Query
# -----------------------------
def query_rag_system(query_text, vector_store):

    llm = ChatOllama(
        model="llama3"
    )

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 5,
            "fetch_k": 20,
        },
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are an expert AI assistant.

Answer ONLY using the provided context.

If the answer is not available in the context, respond exactly:

"I don't know based on the provided documents."

Keep your answers concise and accurate.

Context:
{context}

Question:
{question}

Answer:
"""
    )

    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain.invoke(query_text)


# -----------------------------
# Main
# -----------------------------
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

def load_documents(folder_path):
    loader = DirectoryLoader(
        folder_path,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=True,
    )

    documents = loader.load()

    print(f"📄 Loaded {len(documents)} pages")

    return documents
def main():   

    # Windows path
    folder_path = "C:/Users/haide/OneDrive/Documents/Personal"

    if not os.path.exists("./chroma_db"):

        print("📦 No Vector DB found. Creating one...\n")

        docs = load_documents(folder_path)
        print(f"Loaded {len(docs)} documents")

        for doc in docs[:3]:
         print(doc.metadata)


        chunks = split_text(docs)

        vector_store = create_vector_store(chunks)

        print("✅ Vector Database Created Successfully.\n")

    else:

        print("📦 Loading Existing Vector Database...\n")

        vector_store = Chroma(
            persist_directory="./chroma_db",
            embedding_function=embedding_function,
            collection_name="rag_docs",
        )

        print("✅ Vector Database Loaded.\n")

    while True:

        query = input("\n❓ Ask a Question (type 'exit' to quit): ")

        if query.lower() == "exit":
            print("👋 Goodbye!")
            break

        print("\n🤖 Thinking...\n")

        answer = query_rag_system(query, vector_store)

        print("=" * 60)
        print(answer)
        print("=" * 60)


if __name__ == "__main__":
    main()