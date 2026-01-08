from fastapi.testclient import TestClient
from backend.app import app, llm

client = TestClient(app)

def test_chat_endpoint():
    response = client.post("/chat", json={"query": "voltagem"})

    assert response.status_code == 200

    text = response.text

    if llm:
        assert "110V" in text or "informação necessária" in text
    else:
        assert "Erro: LLM não foi inicializado" in text