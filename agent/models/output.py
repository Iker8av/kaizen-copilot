from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, TypeVar

from agent.models.embedded_file import EmbeddedFile
from agent.models.file import File
from agent.models.issue import Issue

class OutputBase(ABC): pass

OutT = TypeVar("OutT", bound=OutputBase)
    
@dataclass
class QueryFormatterOutput(OutputBase):
    embedded_files: List[EmbeddedFile]
    
@dataclass
class FileBaseOutput(OutputBase):
    files: List[File] 
    
@dataclass
class ModelOutput(OutputBase):
    patch: str 

@dataclass
class EmbeddedFileOutput(OutputBase):
    embedded_files: List[EmbeddedFile] 