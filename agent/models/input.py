from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, TypeVar

from agent.models.embedded_file import EmbeddedFile
from agent.models.file import File
from agent.models.issue import Issue

class InputBase(ABC): pass

InT = TypeVar("InT", bound=InputBase)

@dataclass
class QueryFormatterInput(InputBase):
    issue: Issue
    
@dataclass
class FileInput(InputBase):
    files: List[File] 
    
@dataclass
class EmbeddedFileInput(InputBase):
    embedded_files: List[EmbeddedFile] 
    