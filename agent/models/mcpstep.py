from dataclasses import asdict, dataclass, field
from datetime import datetime
from enum import Enum
from typing import Generic, Optional
from uuid import UUID, uuid4

from agent.models.context import Context
from agent.models.input import InT, InputBase
from agent.models.output import OutT, OutputBase

class ROLE(Enum):
    REPO_ADMIN = "REPO_ADMIN"
    QUERY_FORMATTER = "QUERY_FORMATTER"
    DEVELOPER = "DEVELOPER"
    CONTEXTUALIZER = "CONTEXTUALIZER"

@dataclass
class MCPStep(Generic[InT, OutT]):
    agent_name: str
    role: str
    purpose: str
    input_data: InT
    id: UUID = field(default_factory=uuid4)
    output_data: Optional[OutT] = None
    observations: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
        
    def export(self) -> dict:
        return asdict(self)