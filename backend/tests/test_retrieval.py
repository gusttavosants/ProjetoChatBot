from backend.rag_pipeline import get_vector_store, run_retrieval_augmented_generation

def test_retrieval_pipeline():
    vector_store = get_vector_store()
    context = run_retrieval_augmented_generation("voltagem", vector_store)

    assert "110V" in context