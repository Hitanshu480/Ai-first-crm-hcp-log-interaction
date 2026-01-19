from typing import TypedDict, List

class InteractionState(TypedDict):
    hcp_name: str
    topics_discussed: str
    sentiment: str
    materials_shared: List[str]
    follow_up_actions: str

