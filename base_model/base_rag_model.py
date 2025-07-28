from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver

from graph.graph import Graph
from params.agent_params import AgentParams
import re

class BaseRagModel:
    def __init__(self):
        self.params: AgentParams
        self.checkpoint = MemorySaver()
        self.config: dict
        self.graph: Graph

    def initiate_chatbot(self, params: AgentParams):
        self.params = params
        self.config = {
            "configurable": {
                "thread_id": self.params.thread_id,
            }
        }
        self.graph = Graph(params=self.params).setup_graph(checkpoint=self.checkpoint)
        return self


    @staticmethod
    def __remove_think_block(text: str) -> str:
        # Remove everything between <think> and </think>, including the tags
        return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()

    def run(self, messages):
        human_messages = HumanMessage(content=messages)
        response = self.graph.invoke({"messages": [human_messages], "user_information": self.params.user_information}, config=self.config)
        polished_response = self.__remove_think_block(response["messages"][-1].content)
        return polished_response


