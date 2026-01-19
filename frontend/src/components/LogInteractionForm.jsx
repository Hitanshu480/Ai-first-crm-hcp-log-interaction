import { useSelector } from "react-redux";

export default function LogInteractionForm() {
  const data = useSelector((state) => state.interaction);

  return (
    <div>
      <input value={data.hcp_name || ""} disabled />
      <input value={data.topics_discussed || ""} disabled />
      <input value={data.sentiment || ""} disabled />
      <textarea value={data.follow_up_actions || ""} disabled />
    </div>
  );
}

