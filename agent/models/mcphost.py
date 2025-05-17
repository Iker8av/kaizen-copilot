from agent.agents.query_formatter import QueryFormatter
from agent.models.input import InputBase
from agent.models.issue import Issue
from agent.models.mcplog import MCPLog
from agent.models.mcpstep import MCPStep
from agent.models.output import FileBaseOutput


class MCPHost:
    def __init__(self):
        self.log = MCPLog()
        # self.agents: dict[str, str] = {
        #     # Define Agents
        # }
        # self.tools = dict[str, str] = {
            
        # }
        
        self.workflows = {
            "issue_resolution": [QueryFormatter()],
        }

    def run_workflow(self, name: str, initial_input: InputBase):
        agents = self.workflows.get(name, [])
        input_data = initial_input
        for agent in agents:
            output_data = agent.run(input_data)
            step = MCPStep(
                agent_name=agent.__class__.__name__,
                role=agent.role,
                purpose=agent.purpose,
                input_data=input_data,
                output_data=output_data,
            )
            self.log.add_step(step)
            input_data = output_data  # se convierte en input del siguiente paso

    def get_log(self) -> MCPLog:
        return self.log