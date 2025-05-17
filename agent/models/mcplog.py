from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from agent.models.mcpstep import MCPStep
from agent.models.output import OutputBase

@dataclass
class MCPLog():
    id: UUID = field(default_factory=uuid4)
    steps: List[MCPStep] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    
    def get_latest(self) -> MCPStep:
        return self.steps[-1]
    
    def latest_output(self) -> Optional[OutputBase]:
        return self.steps[-1].output_data if self.steps else None

    def get_context(self) -> dict:
        context = {}
        for step in self.steps:
            if isinstance(step.output_data, dict):
                context.update(step.output_data)
        return context
    
    def add_step(self, step: MCPStep):
        self.steps.append(step)
        pass
    
    def export(self) -> dict[str, any]:
        return asdict(self)