import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from params.agent_params import AgentParams

load_dotenv()

class BaseLLM:
    def __init__(self, params: AgentParams):
        self.params = params
        self.llm = ChatGroq(model=params.groq_model, api_key=params.groq_api_key)
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "{system}"),
                ("system", "Here is the user information: {user_information}"),
                MessagesPlaceholder("messages"),

            ]
        )

    def get_llm(self):
        chain = self.prompt | self.llm.bind_tools(self.params.tools)
        return chain
