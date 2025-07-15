from typing import Optional

from langgraph.graph.message import add_messages
from typing_extensions import TypedDict, List, Annotated
from langchain_core.messages import BaseMessage
import sys

class State(TypedDict):
    """Represent the structure of the state used in the graph workflow."""
    messages: Annotated[List[BaseMessage], add_messages]
    summary: str
    user_information: dict


def get_size_in_kb(obj) -> float:
    """Recursively calculate size of Python object in kilobytesss."""
    seen_ids = set()

    def sizeof(o):
        if id(o) in seen_ids:
            return 0
        seen_ids.add(id(o))
        size = sys.getsizeof(o)

        if isinstance(o, dict):
            size += sum(sizeof(k) + sizeof(v) for k, v in o.items())
        elif isinstance(o, (list, tuple, set, frozenset)):
            size += sum(sizeof(i) for i in o)

        return size

    total_size_bytes = sizeof(obj)
    return total_size_bytes / 1024  # in KB