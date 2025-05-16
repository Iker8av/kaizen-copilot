
from dataclasses import dataclass
import datetime
from enum import Enum
from uuid import UUID

from agent.models.context import Context
from agent.models.input import InputBase
from agent.models.output import OutputBase

class ROLE(Enum):
    REPO_ADMIN = "REPO_ADMIN"
    QUERY_FORMATTER = "QUERY_FORMATTER"
    DEVELOPER = "DEVELOPER"
    CONTEXTUALIZER = "CONTEXTUALIZER"

@dataclass
class MCPStep():
    id: UUID
    role: ROLE
    purpose: str
    obesrvations: str
    input_data: InputBase
    context: Context
    output: OutputBase
    created_at: datetime
    
    def export(self) -> dict[str, any]:
        pass