from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from agent.models.file import File
from agent.models.issue import Issue

class OutputBase(ABC):
    @abstractmethod
    def get_output() -> dict[str, any]:
        pass
    
@dataclass
class FileBaseOutput(OutputBase):
    files: List[File] 
    
@dataclass
class ModelOutput(OutputBase):
    patch: str 