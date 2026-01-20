import React from "react";
import "./App.css";

function App() {
  return (
    <div className="app-container">
      <header className="header">
        AI-First CRM – Log Interaction
      </header>

      <div className="main-layout">
        {/* LEFT: FORM */}
        <div className="form-panel">
          <h3>Interaction Details</h3>

          <label>HCP Name</label>
          <input type="text" value="Dr John" readOnly />

          <label>Interaction Type</label>
          <input type="text" value="In-person Visit" readOnly />

          <label>Sentiment</label>
          <input type="text" value="Positive" readOnly />

          <label>Summary</label>
          <textarea
            rows="4"
            value="Discussed product efficacy and dosage."
            readOnly
          />
        </div>

        {/* RIGHT: CHAT */}
        <div className="chat-panel">
          <h3>AI Assistant</h3>

          <div className="chat-box">
            <div className="bot-msg">
              Hello! Tell me about your interaction with the HCP.
            </div>
          </div>

          <input
            className="chat-input"
            placeholder="Type here... e.g. Met Dr John, sentiment was positive"
          />
        </div>
      </div>
    </div>
  );
}

export default App;
