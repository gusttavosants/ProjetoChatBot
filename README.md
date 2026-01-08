# 🤖 RAG ChatBot

A sophisticated chatbot implementation using Retrieval Augmented Generation (RAG) to provide intelligent responses based on SQL database content and vectorized documents stored in ChromaDB.

## ✨ Features

- **Intelligent Q&A**: Answers questions using contextual information from SQL database and document embeddings
- **RAG Pipeline**: Combines retrieval from multiple sources with LLM generation
- **Streaming Responses**: Real-time response streaming for better user experience
- **Modern UI**: Clean React interface with Vite for fast development
- **Comprehensive Testing**: Automated test suite for backend functionality
- **CORS Enabled**: Proper cross-origin support for frontend-backend communication

## 🏗️ Architecture

```
ProjetoChatBot/
│
├── backend/
│   ├── app.py               # FastAPI application and endpoints
│   ├── rag_pipeline.py      # RAG pipeline implementation
│   ├── database/            # SQLite database with knowledge base
│   ├── chroma_db/           # ChromaDB vector storage
│   ├── .env                 # Environment configuration
│   └── tests/               # Comprehensive test suite
│       ├── test_chat.py
│       └── test_rag_pipeline.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── .gitignore               # Git ignore rules
├── requirements.txt         # Python dependencies
└── README.md
```

## 🚀 Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **LangChain** - LLM orchestration framework
- **ChromaDB** - Vector database for embeddings
- **Sentence Transformers** - Text embedding models
- **Google Gemini** - Large language model via LangChain
- **Python-dotenv** - Environment variable management
- **Pydantic** - Data validation

### Frontend
- **React** - UI library
- **Vite** - Build tool and dev server

### Testing
- **Pytest** - Test framework
- **Pytest-asyncio** - Async testing support
- **HTTPX** - HTTP client for testing

## 📦 Installation

### Prerequisites
- Python 3.8+
- Node.js 16+
- Google Gemini API key

### Backend Setup

1. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # or
   source venv/bin/activate  # Linux/Mac
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   Create `backend/.env`:
   ```env
   GEMINI_API_KEY=your_google_gemini_api_key_here
   ```

4. **Run backend server**
   ```bash
   uvicorn backend.app:app --host 0.0.0.0 --port 8000 --reload
   ```
   API available at: http://localhost:8000

### Frontend Setup

1. **Install dependencies**
   ```bash
   cd frontend
   npm install
   ```

2. **Run development server**
   ```bash
   npm run dev
   ```
   Frontend available at: http://localhost:5173

## 🧪 Testing

Run the comprehensive test suite:

```bash
python -m pytest backend/tests/ -v
```

Tests cover:
- Chat endpoint functionality
- RAG pipeline components
- Database operations
- Vector store operations
- Error handling

## 🔄 RAG Pipeline

The RAG implementation follows this workflow:

1. **Query Reception**: Receive user question from frontend
2. **SQL Retrieval**: Query structured data from SQLite database
3. **Vector Search**: Find relevant documents using ChromaDB embeddings
4. **Context Building**: Combine SQL results with vector context
5. **LLM Generation**: Send enriched prompt to Google Gemini
6. **Response Streaming**: Return generated answer to frontend

## 🌐 System Flow

1. User inputs question in React interface
2. Frontend sends POST request to `/chat` endpoint
3. Backend processes query through RAG pipeline
4. SQL database provides structured knowledge
5. ChromaDB supplies contextual document snippets
6. Gemini generates coherent, informed response
7. Streaming response delivered back to user

## 📡 API Endpoints

### POST /chat
Send a question and receive an AI-generated response using RAG.

**Request Body:**
```json
{
  "query": "Tell me about the product warranty information"
}
```

**Response:** Streaming text response with contextual answer

**Error Response:**
```json
"Erro: LLM não foi inicializado. Verifique GEMINI_API_KEY."
```

## 📋 Dependencies

### Backend Requirements
```
fastapi
uvicorn[standard]
python-dotenv
pydantic

langchain-google-genai
langchain
langchain-core
langchain-community
chromadb
sentence-transformers

pytest
pytest-asyncio
httpx
```

### Frontend Dependencies
See `frontend/package.json`

## 🔒 Environment Variables

Create `backend/.env`:
```
GEMINI_API_KEY=your_api_key_from_google_ai_studio
```

## 📜 License

This project was developed for technical assessment purposes.

## 👤 Author

**Gustavo Santos**
- Backend Developer
- Python | FastAPI | LangChain
- GitHub: https://github.com/gusttavosants
