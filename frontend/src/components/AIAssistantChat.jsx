import { useState } from "react";
import { useDispatch } from "react-redux";
import { setInteraction } from "../redux/interactionSlice";

export default function AIAssistantChat() {
  const [text, setText] = useState("");
  const dispatch = useDispatch();

  const sendMessage = async () => {
    const res = await fetch("http://localhost:8000/agent/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text }),
    });
    const data = await res.json();
    dispatch(setInteraction(data));
    setText("");
  };

  return (
    <div>
      <textarea
        placeholder="Describe interaction..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

