from typing import Dict, List
from agent.agents.embedding_model import EmbeddingModel
from agent.agents.query_formatter import QueryFormatter
from agent.models.agentbase import AgentBase
from agent.models.context import Context
from agent.models.input import InputBase
from agent.models.mcplog import MCPLog
from agent.models.mcpstep import MCPStep

class MCPHost:
    def __init__(self):
        self.__log = MCPLog()
        self.workflows: Dict[str, List[AgentBase]] = {
            "issue_resolution": [QueryFormatter(), EmbeddingModel()],
        }

    def run_workflow(self, name: str, initial_input: InputBase):
        agents = self.workflows.get(name, [])
        input_data = initial_input
        context = Context(name)
        
        for agent in agents:
            output_data, context = agent.run(input_data, context)
            step = MCPStep(
                agent_name=agent.__class__.__name__,
                tool=agent.tool,
                role=agent.role,
                purpose=agent.purpose,
                context=context,
                input_data=input_data,
                output_data=output_data,
            )
            self.__log.add_step(step)
            input_data = output_data  
            
    def get_log(self) -> MCPLog:
        return self.__log