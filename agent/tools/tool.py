from abc import ABC, abstractmethod
from typing import Generic
from sentence_transformers import SentenceTransformer

from agent.models.context import Context
from agent.models.embedded_file import EmbeddedFile

class Tool(ABC):    
    @abstractmethod
    def execute(workflow: str, inputs: any, context: Context) -> any:
        pass