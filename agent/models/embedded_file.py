
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Tuple
from uuid import UUID


@dataclass
class EmbeddedFile():
    id: UUID
    document: str
    embeddings: List[float]
    content: Optional[str]
    metadata: "Metadata"
    
    def convert_to_file(self) -> bool:
        pass
    
    @staticmethod
    def get_elements(files: List["EmbeddedFile"]) -> Tuple[List[UUID], List[str], List[List[float]], List[dict[str, str]]]:
        pass
    
@dataclass
class Metadata():
    name: str
    path: str
    extension: str
    
    def export(self) -> dict[str, str]:
        pass