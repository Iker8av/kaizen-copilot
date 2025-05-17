
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from uuid import UUID, uuid4

@dataclass
class EmbeddedFile():
    document: str
    metadata: "Metadata"
    embeddings: List[float] = field(default_factory=list)
    id: UUID = field(default_factory=uuid4)
    
    def convert_to_file(self) -> bool:
        pass
    
    @staticmethod
    def get_elements(files: List["EmbeddedFile"]) -> Tuple[List[UUID], List[str], List[List[float]], List[Dict[str, str]]]:
        pass
    
class Metadata():
    def __init__(self, extension: Optional[str]):
        self.extension: str = extension
        self.name: str = ""
        self.path: str = ""
        pass