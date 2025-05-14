from dataclasses import dataclass
import datetime
from typing import List
from uuid import UUID

from agent.models.mcpstep import MCPStep

@dataclass
class MCPLog():
    id: UUID
    steps: List[MCPStep]
    created_at: datetime
    
    def get_latest() -> MCPStep:
        pass
    
    def append_step(step: MCPStep) -> None:
        pass
    
    def export() -> dict[str, any]:
        pass