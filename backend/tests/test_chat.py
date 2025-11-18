from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_chat_endpoint():
    response = client.post("/chat", json={"query": "voltagem"})

    assert response.status_code == 200

    text = response.text

    assert "110V" in text or "informação necessária" in text