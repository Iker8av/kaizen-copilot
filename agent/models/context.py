
from dataclasses import dataclass
from typing import List

from agent.models.file import File
from agent.models.issue import Issue

@dataclass
class Context():
    issue: Issue
    retrieved_files: List[File]
    
    def all_files_completed(self) -> bool:
        pass