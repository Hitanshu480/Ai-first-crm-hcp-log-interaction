from langgraph.graph import StateGraph
from .state import InteractionState
from .tools import (
    log_interaction_tool,
    edit_interaction_tool,
    validate_interaction_tool,
    compliance_tool,
    followup_tool
)

def build_graph():
    graph = StateGraph(InteractionState)

    # Nodes
    graph.add_node("log", log_interaction_tool)
    graph.add_node("edit", edit_interaction_tool)
    graph.add_node("validate", validate_interaction_tool)
    graph.add_node("compliance", compliance_tool)

    # Entry point
    graph.set_entry_point("log")

    # Flow
    graph.add_edge("log", "validate")
    graph.add_edge("edit", "validate")
    graph.add_edge("validate", "compliance")

    # FINAL NODE (no dead-end)
    graph.add_node("final", followup_tool)
    graph.add_edge("compliance", "final")

    # IMPORTANT: declare final node as output
    graph.set_finish_point("final")

    return graph.compile()
