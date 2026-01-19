import LogInteractionForm from "./components/LogInteractionForm";
import AIAssistantChat from "./components/AIAssistantChat";

export default function App() {
  return (
    <div style={{ display: "flex", gap: "20px" }}>
      <LogInteractionForm />
      <AIAssistantChat />
    </div>
  );
}

