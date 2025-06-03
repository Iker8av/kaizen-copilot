from abc import ABC
from dataclasses import dataclass
from typing import List, TypeVar

from chromadb import Where

from agent.models.embedded_file import EmbeddedFile
from agent.models.file import File

class OutputBase(ABC): pass

OutT = TypeVar("OutT", bound=OutputBase)
    
@dataclass
class QueryFormatterOutput(OutputBase):
    queries: List[str]
    conditionals: List[Where]
    
@dataclass
class FileBaseOutput(OutputBase):
    files: List[File] 

@dataclass
class EmbeddedFileOutput(OutputBase):
    embedded_files: List[EmbeddedFile] 
    
@dataclass
class LLMDeveloperOutput(OutputBase):
    fixed_code: str
    comments:str