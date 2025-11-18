from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import AsyncGenerator
import os
from dotenv import load_dotenv

from backend.rag_pipeline import get_vector_store

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

from backend.rag_pipeline import get_vector_store

load_dotenv()

app = FastAPI(title="Chatbot RAG SQL API")

# CORS para Vite/CRA
origins = ["http://localhost:5173", "http://localhost:3000", "http://127.0.0.1:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carrega o vector store
print("[RAG] Carregando Vector Store...")
vector_store = get_vector_store()

# Inicializa o LLM Gemini
try:
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    print("[RAG] LLM inicializado com sucesso!")
except Exception as e:
    print(f"[RAG] ERRO ao inicializar LLM: {e}")
    llm = None

# Modelo Pydantic
class QueryModel(BaseModel):
    query: str

# Prompt template
SYSTEM_TEMPLATE = """
Você é um assistente RAG conectado a um banco SQL.
Responda apenas com base no contexto fornecido abaixo.

Se não encontrar a resposta no contexto, responda:
"Não consegui encontrar a informação necessária no meu banco de conhecimento."

CONTEXTO:
{context}
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_TEMPLATE),
    ("human", "{query}")
])

# Função de retrieval
def retrieval_step(query: str):
    results = vector_store.similarity_search(query, k=3)
    context = "\n\n---\n\n".join([doc.page_content for doc in results])
    return context

# Pipeline RAG
rag_chain = (
    {"context": lambda x: retrieval_step(x["query"]), "query": lambda x: x["query"]}
    | prompt
    | llm.with_config({"tags": ["generation"]})
    | StrOutputParser()
)

# Endpoint de streaming
@app.post("/chat")
async def chat_endpoint(query_data: QueryModel):
    if not llm:
        return StreamingResponse(
            iter(["Erro: LLM não foi inicializado. Verifique GEMINI_API_KEY."]),
            media_type="text/plain"
        )

    stream = rag_chain.astream({"query": query_data.query})

    async def generate() -> AsyncGenerator[str, None]:
        async for chunk in stream:
            yield chunk

    return StreamingResponse(generate(), media_type="text/plain")


# Rodar local
if __name__ == "__main__":
    import uvicorn
    print("[RAG] Servidor FastAPI rodando em http://localhost:8000")
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
