
from dataclasses import dataclass
from enum import Enum
from typing import Optional

from agent.models.embedded_file import EmbeddedFile

class FILE_TYPE(Enum):
    MAIN_FILE = "MAIN_FILE"
    DEPENDENCY = "DEPENDENCY"

@dataclass
class File():
    name: str
    path: str
    content: str
    content: Optional[str]
    file_type: FILE_TYPE
    
    def is_complete(self) -> bool:
        pass
    
    def convert_to_embedding(self) -> EmbeddedFile:
        pass
