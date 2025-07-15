from params.agent_params import AgentParams
from base_model.base_rag_model import BaseRagModel
class SimpleRag(BaseRagModel):
    def initiate_chatbot(self, params: AgentParams):
        return super().initiate_chatbot(params)
