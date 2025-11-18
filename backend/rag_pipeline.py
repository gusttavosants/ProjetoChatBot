import os
import sqlite3
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

# --- CONFIGURAÇÃO ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database', 'knowledge.db')
CHROMA_PATH = os.path.join(BASE_DIR, "chroma_db")
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"


# -----------------------------
# FUNÇÃO 1: CRIAÇÃO E POPULAÇÃO DO BANCO SQL
# -----------------------------
def setup_database_if_not_exists():
    db_folder = os.path.join(BASE_DIR, "database")
    os.makedirs(db_folder, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documentos (
        id INTEGER PRIMARY KEY,
        titulo TEXT,
        conteudo TEXT,
        categoria TEXT
    );
    """)
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM documentos")
    count = cursor.fetchone()[0]

    if count == 0:
        knowledge_data = [
            ('Manual do Produto X', 'O produto X opera em voltagem 110V e possui garantia de 1 ano. Para suporte, ligue 4002-8922.', 'manual'),
            ('Política de Devolução', 'Devoluções são aceitas em até 7 dias após a compra, desde que o produto esteja na embalagem original e sem sinais de uso.', 'legal'),
            ('Especificações Técnicas', 'A bateria do modelo Y dura aproximadamente 12 horas e o tempo de recarga total é de 2 horas. Utilize apenas carregadores homologados.', 'tecnico'),
        ]
        cursor.executemany("INSERT INTO documentos (titulo, conteudo, categoria) VALUES (?, ?, ?)", knowledge_data)
        conn.commit()

    conn.close()


# -----------------------------
# FUNÇÃO 2: CARREGAR DOCUMENTOS
# -----------------------------
def load_documents_from_sql():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT titulo, conteudo FROM documentos")
    rows = cursor.fetchall()
    conn.close()

    documents = [f"Título: {titulo}\nConteúdo: {conteudo}" for titulo, conteudo in rows]
    return documents


# -----------------------------
# FUNÇÃO 3: DIVIDIR DOCUMENTOS EM CHUNKS
# -----------------------------
def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, length_function=len)
    chunks = splitter.create_documents(documents)
    return chunks


# -----------------------------
# FUNÇÃO 4: CRIAR OU CARREGAR VECTOR STORE
# -----------------------------
def get_vector_store():
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

    if not os.path.exists(CHROMA_PATH):
        print("[RAG] Index não encontrado. Criando novo Index...")
        documents = load_documents_from_sql()
        chunks = split_documents(documents)
        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=CHROMA_PATH
        )
        print(f"[RAG] Index criado e salvo em: {CHROMA_PATH}")
    else:
        print("[RAG] Index encontrado. Carregando index existente...")
        vector_store = Chroma(
            persist_directory=CHROMA_PATH,
            embedding_function=embeddings
        )
        print("[RAG] Index carregado com sucesso.")

    return vector_store


# -----------------------------
# FUNÇÃO 5: TESTE DE RETRIEVAL
# -----------------------------

def run_retrieval_augmented_generation(query: str, vector_store):
    results = vector_store.similarity_search(query, k=3)
    context = "\n\n---\n\n".join([doc.page_content for doc in results])
    return context

# -----------------------------
# EXECUÇÃO LOCAL
# -----------------------------
if __name__ == "__main__":
    setup_database_if_not_exists()
    get_vector_store()
    print("[RAG] Pipeline RAG pronto!")
