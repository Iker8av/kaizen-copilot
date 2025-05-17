from abc import ABC, abstractmethod
from typing import Generic, Optional
from agent.models.context import Context
from agent.models.input import InT, InputBase
from agent.models.mcpstep import ROLE, MCPStep
from agent.models.output import OutT, OutputBase

class AgentBase(ABC, Generic[InT, OutT]): 
    def __init__(self):
        self.agent_name: str = ""
        self.role: ROLE = None
        self.agent_input: InputBase = None
        self.output: OutputBase = None
        self.context: Context = None
        self.purpose: str = ""
        self.step: Optional[MCPStep] = None

    @abstractmethod
    def run(self, input_data: InT) -> OutT:
        pass