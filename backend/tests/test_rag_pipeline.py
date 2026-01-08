from backend.rag_pipeline import setup_database_if_not_exists, load_documents_from_sql, split_documents, get_vector_store

def test_setup_database():
    setup_database_if_not_exists()
    # Test that documents are inserted
    from backend.rag_pipeline import DB_PATH
    import sqlite3
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM documentos")
    count = cursor.fetchone()[0]
    conn.close()
    assert count > 0

def test_load_documents():
    documents = load_documents_from_sql()
    assert isinstance(documents, list)
    assert len(documents) > 0
    assert "Título:" in documents[0]

def test_split_documents():
    documents = load_documents_from_sql()
    chunks = split_documents(documents)
    assert len(chunks) > 0
    # Assuming chunks are created

def test_get_vector_store():
    vector_store = get_vector_store()
    assert vector_store is not None
    # Test similarity search
    results = vector_store.similarity_search("voltagem", k=1)
    assert len(results) > 0