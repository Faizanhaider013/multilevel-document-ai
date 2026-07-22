# 📚 Multi-Level Document RAG System

An AI-powered Retrieval-Augmented Generation (RAG) application that enables users to chat with their personal documents using a locally running Large Language Model (LLM). The system indexes documents into a vector database and retrieves the most relevant context to answer user queries accurately while minimizing hallucinations.

---

# 🚀 Features

* 📄 Load documents from a local folder
* 🔍 Semantic search using vector embeddings
* ✂️ Intelligent document chunking
* 🧠 Local LLM inference with Ollama (Llama 3)
* 💾 Persistent Chroma vector database
* 🤖 Context-aware question answering
* 🔒 Fully local processing (no API required)

---

# 🏗️ Architecture

```
Documents
     │
     ▼
Document Loader
     │
     ▼
Text Splitter
(RecursiveCharacterTextSplitter)
     │
     ▼
Sentence Embeddings
(all-MiniLM-L6-v2)
     │
     ▼
Chroma Vector Database
     │
     ▼
Retriever (MMR Similarity Search)
     │
     ▼
Prompt Template
     │
     ▼
Llama 3 (Ollama)
     │
     ▼
Generated Answer
```

---

# 🛠️ Tech Stack

* Python
* LangChain
* LangChain Community
* LangChain Chroma
* LangChain HuggingFace
* LangChain Ollama
* ChromaDB
* Hugging Face Sentence Transformers
* Ollama
* Llama 3
* PyPDF
* Python-Docx

---

# 📂 Project Structure

```
.
├── main.py
├── chroma_db/
├── documents/
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/multilevel-document-rag.git
cd multilevel-document-rag
```

### Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

# 📥 Install Ollama

Download and install Ollama from:

https://ollama.com

Pull the Llama 3 model:

```bash
ollama pull llama3
```

Verify that Ollama is running:

```bash
ollama list
```

---

# 📄 Add Your Documents

Place your documents inside the desired folder (for example):

```
Documents/
├── AI Notes.pdf
├── Resume.pdf
├── NLP.docx
└── Research.txt
```

Update the folder path in `main.py`:

```python
folder_path = r"C:\Users\YourName\Documents"
```

---

# ▶️ Run the Project

```bash
python main.py
```

Example:

```
❓ Ask a Question:
Summarize the uploaded documents.

🤖 Thinking...

🧠 Answer:
...
```

---

# 🔄 How It Works

1. Load documents from a local directory.
2. Extract text from supported document formats.
3. Split documents into overlapping chunks.
4. Generate embeddings for each chunk using Hugging Face Sentence Transformers.
5. Store embeddings in a persistent Chroma vector database.
6. Convert the user's question into an embedding.
7. Retrieve the most relevant document chunks using semantic similarity search.
8. Pass the retrieved context and the user query to the Llama 3 model through Ollama.
9. Generate an answer based only on the retrieved document context.

---

# 📌 Current Capabilities

* Semantic document search
* Context-aware question answering
* Persistent vector storage
* Local inference without external APIs
* Multiple document ingestion
* Intelligent chunking
* MMR-based retrieval

---

# 🔮 Future Improvements

* Hybrid Search (BM25 + Vector Search)
* Metadata filtering
* Source citations with page numbers
* Multi-modal document support
* OCR for scanned PDFs
* Conversation memory
* Incremental indexing
* Web interface using Streamlit or FastAPI
* Reranking using BGE or Cohere models
* Support for PPTX, Excel, and HTML documents

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Semantic Search
* Embedding Models
* Prompt Engineering
* Local LLM Deployment
* Document Processing Pipelines
* LangChain Framework
* AI Application Development

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Faizan Haider**

AI/ML Engineer | AI Automation | RAG Systems | NLP | React | FastAPI

Feel free to contribute, raise issues, or suggest improvements.
