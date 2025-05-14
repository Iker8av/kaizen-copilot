
from dataclasses import dataclass
from enum import Enum

class FILE_TYPE(Enum):
    MAIN_FILE = "MAIN_FILE"
    DEPENDENCY = "DEPENDENCY"

@dataclass
class File():
    name: str
    path: str
    content: str
    file_type: FILE_TYPE
    
    def is_complete() -> bool:
        pass