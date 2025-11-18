import React, { useState } from "react";

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMsg = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMsg]);

    setInput("");
    setLoading(true);

    const response = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: input }),
    });

    const reader = response.body.getReader();
    let aiText = "";
    const decoder = new TextDecoder("utf-8");

    while (true) {
      const { value, done } = await reader.read();
      if (done) break;

      aiText += decoder.decode(value);

      setMessages((prev) => {
        const updated = [...prev];
        const last = updated[updated.length - 1];

        if (last.sender === "ai") {
          last.text = aiText;
          return [...updated];
        }

        return [...updated, { sender: "ai", text: aiText }];
      });
    }

    setLoading(false);
  };

  return (
    <div className="app-container">
      <h1 className="header">Chat RAG SQL</h1>

      <div className="chat-box">
        {messages.map((msg, i) => (
          <div
            key={i}
            className={`message ${msg.sender === "user" ? "user" : "bot"}`}
          >
            {msg.text}
          </div>
        ))}

        {loading && <p className="loading">Gerando...</p>}
      </div>

      <div className="input-area">
        <input
          className="input-field"
          value={input}
          placeholder="Digite sua pergunta..."
          onChange={(e) => setInput(e.target.value)}
        />

        <button className="send-btn" onClick={sendMessage}>
          Enviar
        </button>
      </div>
    </div>
  );
}

export default App;