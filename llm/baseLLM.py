import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from params.agent_params import AgentParams

load_dotenv()

class BaseLLM:
    def __init__(self, params: AgentParams):
        self.params = params
        self.llm = ChatOpenAI(
            model=self.params.model,
            api_key=self.params.api_key,
            base_url=self.params.base_url,
            temperature=self.params.temperature
        )
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