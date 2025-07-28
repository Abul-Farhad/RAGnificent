from langchain_core.messages import HumanMessage, RemoveMessage
from llm.baseLLM import BaseLLM
from params.agent_params import AgentParams
from state.state import State

class BaseAgentNode:
    def __init__(self, params: AgentParams):
        self.llm = BaseLLM(params).get_llm()
        self.params = params

    def get_agent(self, state: State):
        pass


class AgentNode(BaseAgentNode):

    def get_agent(self, state: State) -> dict:
        """
        Retrieve the agent's response based on the current state.

        Args:
            state (State): The current state containing messages.

        Returns:
            dict: A dictionary containing the agent's response.
        """
        # print("--- Agent Node Called ---")
        system_message = self.params.system_prompt
        summary = state.get("summary", "")
        if summary:
            system_message += f"Summary of the conversation so far: {summary}\n"

        user_information = state.get("user_information", {})
        response = self.llm.invoke({"system": system_message, "messages": state["messages"], "user_information": user_information})
        return {"messages": [response]}

class SummarizerNode(BaseAgentNode):

    def get_agent(self, state: State) -> dict:
        """
        Summarize the conversation based on the current state.

        Args:
            state (State): The current state containing messages.

        Returns:
            dict: A dictionary containing the summary of the conversation.
        """
        # print("--- Summarizer Node Called ---")
        system_message = self.params.summary_prompt
        summary = state.get("summary", "")
        if summary:
            summary_message = (
                f"This is summary of the conversation to date: {summary}\n\n"
                "Extend the summary by taking into account the new messages above:"
            )
        else:
            summary_message = "Create a summary of the conversation above:"
        user_information = state.get("user_information", {})
        response = self.llm.invoke({"system": system_message, "messages": state["messages"] + [HumanMessage(content=summary_message)], "user_information": user_information})
        delete_messages = [RemoveMessage(id=m.id) for m in state["messages"][:-2]]
        # print("delete_messages:", delete_messages)
        return {"messages": delete_messages, "summary": response.content}
