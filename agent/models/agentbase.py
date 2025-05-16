from dataclasses import dataclass

from agent.models.input import InputBase
from agent.models.mcpstep import ROLE, MCPStep
from agent.models.output import OutputBase


@dataclass
class AgentBase:
    agent_input: InputBase
    output: OutputBase
    role: ROLE
    purpose: str
    step: MCPStep

    def run(self, prev_step: MCPStep) -> MCPStep:
        pass