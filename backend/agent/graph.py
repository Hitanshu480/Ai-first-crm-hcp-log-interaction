from langgraph.graph import StateGraph, END
from .state import InteractionState
from .tools import (
    log_interaction_tool,
    edit_interaction_tool,
    validate_interaction_tool,
    compliance_tool,
)

def build_graph():
    graph = StateGraph(InteractionState)

    graph.add_node("log", log_interaction_tool)
    graph.add_node("edit", edit_interaction_tool)
    graph.add_node("validate", validate_interaction_tool)
    graph.add_node("compliance", compliance_tool)

    graph.set_entry_point("log")

    graph.add_edge("log", "validate")
    graph.add_edge("edit", "validate")
    graph.add_edge("validate", "compliance")
    graph.add_edge("compliance", END)

    return graph.compile()
