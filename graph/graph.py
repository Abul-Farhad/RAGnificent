from typing import Literal
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from nodes.nodes import AgentNode, SummarizerNode
from params.agent_params import AgentParams
from state.state import State


class Graph:
    """
    A class to build and compile a state graph for an agentic AI workflow.
    """

    def __init__(self, params: AgentParams):
        self.params = params
        self.graph_builder = StateGraph(State)


    def setup_graph(self, checkpoint=None):
        """
        Set up the graph with a basic chatbot node.
        """

        def agent_conditions(state: State) -> str:
            # First check if tool needs to be called
            tool_result = tools_condition(state)
            if tool_result != END:
                return tool_result

            # Then check if summarizer should be called
            if len(state["messages"]) > 6:
                return "summarizer"

            # Otherwise, finish
            return END

        self.agent_node = AgentNode(params=self.params)
        self.summarizer_node = SummarizerNode(params=self.params)
        self.graph_builder.add_node("agent", self.agent_node.get_agent)
        self.graph_builder.add_node("summarizer", self.summarizer_node.get_agent)
        self.graph_builder.add_node("tools", ToolNode(self.params.tools))
        self.graph_builder.add_edge(START, "agent")
        self.graph_builder.add_conditional_edges(
            "agent",
            agent_conditions
        )
        self.graph_builder.add_edge("tools", "agent")
        self.graph_builder.add_edge("summarizer", END)
        if not checkpoint:
            return self.graph_builder.compile()
        return self.graph_builder.compile(checkpointer=checkpoint)


