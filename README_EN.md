RAG ChatBot — FastAPI + LangChain + ChromaDB + React

This project implements an intelligent chatbot using RAG (Retrieval Augmented Generation) to answer user questions based on information stored in a SQL database and vectorized documents in ChromaDB.

It consists of:

Backend (FastAPI) — RAG pipeline, embeddings, retrieval, SQL access, and REST API

Frontend (React) — simple chat interface

Testing (Pytest) — API tests

LLM (Google Gemini) — used for contextual response generation

📂 Project Structure
ProjetoChatBotComRAG/
│
├── backend/
│   ├── app.py               # FastAPI server and endpoints
│   ├── rag_pipeline.py      # RAG pipeline (embeddings, retrieval, LLM)
│   ├── database/            # SQL database + scripts
│   ├── chroma_db/           # Local ChromaDB storage
│   ├── .env                 # Environment configuration
│   └── tests/               # Pytest test suite
│
└── frontend/
    ├── src/
    ├── public/
    └── package.json

🚀 Tech Stack
Backend

FastAPI

LangChain

ChromaDB

Sentence Transformers

Google Gemini (google-genai)

Python-dotenv

Pydantic

Frontend

React + Vite

Axios

Testing

Pytest

Pytest-asyncio

HTTPX

⚙️ Backend Setup
1️⃣ Create and activate the virtual environment
cd backend
python -m venv venv
venv\Scripts\activate   # Windows

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Create the .env file
GEMINI_API_KEY=YOUR_API_KEY
DB_PATH=./database/database.db
CHROMA_PATH=./chroma_db

4️⃣ Start the server
uvicorn app:app --reload


API available at:
👉 http://localhost:8000

🤖 RAG Pipeline Overview

The RAG pipeline implemented in rag_pipeline.py follows this flow:

Receive the question from the frontend

Query SQL database for relevant entries

Retrieve vector-based context from ChromaDB

Build a combined context-aware prompt

Send prompt to Google Gemini

Return final enriched response to the client

🧪 Running Tests

Run all tests with:

pytest -v


Tests include:

/chat endpoint

RAG pipeline logic

Basic integration tests

🖥️ Frontend Setup
cd frontend
npm install
npm run dev


Frontend runs on:
👉 http://localhost:5173

🌐 Full System Flow

User sends a question in the React UI

Backend receives and processes it via RAG

SQL database is queried first

ChromaDB retrieves vector embeddings

Gemini generates final answer

Response is returned to the UI

📡 Main Endpoint
POST /chat

Request:

{
  "question": "Tell me about the stored product data."
}


Response:
Natural language answer generated using retrieved SQL + vector context.

📦 Backend Dependencies
fastapi
uvicorn[standard]
python-dotenv
pydantic

google-genai

langchain
langchain-core
langchain-community
chromadb
sentence-transformers

pytest
pytest-asyncio
httpx

📜 License

This project was developed for a technical assessment.

👤 Author

Gustavo Santos
Backend Developer — Python | FastAPI
GitHub: https://github.com/gusttavosants
