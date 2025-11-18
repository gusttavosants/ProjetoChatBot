ChatBot com RAG — FastAPI + LangChain + ChromaDB + React

Este projeto implementa um chatbot inteligente utilizando RAG (Retrieval Augmented Generation) para responder perguntas com base em informações armazenadas em um banco de dados SQL e documentos vetorizados no ChromaDB.

Ele é composto por:

Backend (FastAPI) — pipeline RAG, embeddings, retrieval, conexão SQL e API de chat

Frontend (React) — interface simples para enviar perguntas e receber respostas

Testes (Pytest) — testes de API

LLM (Google Gemini) — usado para geração de respostas com contexto recuperado

📂 Arquitetura do Projeto
ProjetoChatBotComRAG/
│
├── backend/
│   ├── app.py               # API FastAPI e endpoints
│   ├── rag_pipeline.py      # Pipeline de RAG (embeddings, retrieval, geração)
│   ├── database/            # Scripts + modelo SQL
│   ├── chroma_db/           # Armazenamento local do ChromaDB
│   ├── .env                 # Configurações de ambiente
│   └── tests/               # Testes com Pytest
│
└── frontend/
    ├── src/
    ├── public/
    └── package.json

🚀 Tecnologias Utilizadas
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

Testes

Pytest

Pytest-asyncio

HTTPX

⚙️ Como Rodar o Backend
1️⃣ Criar e ativar o ambiente virtual
cd backend
python -m venv venv
venv\Scripts\activate  # Windows

2️⃣ Instalar dependências
pip install -r requirements.txt

3️⃣ Criar arquivo .env
GEMINI_API_KEY= SUA_CHAVE_AQUI
DB_PATH=./database/database.db
CHROMA_PATH=./chroma_db

4️⃣ Rodar o servidor
uvicorn app:app --reload


Servidor disponível em:
👉 http://localhost:8000

🤖 Pipeline RAG

A lógica de RAG implementada (rag_pipeline.py) segue:

Carregar perguntas do frontend

Buscar contexto no SQL (SQLite/MySQL)

Buscar documentos relevantes no ChromaDB

Construir o prompt com as duas fontes

Enviar para o modelo Gemini

Devolver a resposta estruturada ao frontend

🧪 Rodando os Testes
pytest -v


Testes incluem:

Endpoint /chat

Pipeline de RAG

Integração básica

🖥️ Como Rodar o Frontend
cd frontend
npm install
npm run dev


Disponível em:
👉 http://localhost:5173

🌐 Fluxo Completo

Usuário envia mensagem pelo React

Backend recebe e passa para o pipeline RAG

Recupera dados do banco SQL

Recupera documentos vetorizados do ChromaDB

Envia para o Gemini gerar a resposta

Retorna resposta enriquecida ao frontend

📌 Endpoints Principais
POST /chat

Envia uma pergunta e retorna uma resposta usando RAG.

Exemplo de payload:

{
  "question": "Me fale sobre o histórico armazenado no banco."
}

📦 Requisitos do Projeto

Lista de todas dependências usadas no backend:

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

📜 Licença

Este repositório é apenas para fins de teste técnico.

🙋 Autor

Gustavo Santos
Desenvolvedor Backend | Python | FastAPI
GitHub: https://github.com/gusttavosants
