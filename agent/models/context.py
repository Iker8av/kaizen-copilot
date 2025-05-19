
from dataclasses import dataclass, field
from typing import List

from agent.models.file import File
from agent.models.issue import Issue

@dataclass
class Context():
    workflow: str
    issue: Issue = None
    retrieved_files: List[File] = field(default_factory=list)
    
    def all_files_completed(self) -> bool:
        pass