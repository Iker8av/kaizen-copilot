from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from agent.models.file import File
from agent.models.issue import Issue

class InputBase(ABC):
    @abstractmethod
    def get_input() -> dict[str, any]:
        pass

@dataclass
class QueryFormatterInput(InputBase):
    issue: Issue
    
@dataclass
class FileBaseInput(InputBase):
    files: List[File] 
    
@dataclass
class QueryFormatterInput(InputBase):
    repo_url: str 