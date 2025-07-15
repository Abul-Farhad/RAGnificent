from params.agent_params import AgentParams
from base_model.base_rag_model import BaseRagModel
class SimpleRag(BaseRagModel):
    def __init__(self, params: AgentParams):
        self.params = params
        super().__init__(params)
        # Just testing
