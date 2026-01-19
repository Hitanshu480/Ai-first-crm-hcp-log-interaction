from langgraph.prebuilt import ToolNode
from langgraph.graph import MessageGraph
from langchain_core.messages import HumanMessage
from .tools import (
    log_interaction_tool,
    edit_interaction_tool,
    validate_interaction_tool,
    compliance_tool,
    followup_tool
)

def build_graph():
    tools = [
        log_interaction_tool,
        edit_interaction_tool,
        validate_interaction_tool,
        compliance_tool,
        followup_tool,
    ]

    tool_node = ToolNode(tools)

    graph = MessageGraph()
    graph.add_node("tools", tool_node)
    graph.set_entry_point("tools")

    return graph.compile()
