
from dataclasses import dataclass
from enum import Enum

class FILE_TYPE(Enum):
    MAIN_FILE = "MAIN_FILE"
    DEPENDENCY = "DEPENDENCY"

@dataclass
class File():
    name: str
    path: str
    content: str
    extension: str
    context: str = ""
    file_type: FILE_TYPE = None
    
    def is_complete(self) -> bool:
        pass
    
    def convert_to_embedding(self) -> "EmbeddedFile": # type: ignore
        from agent.models.embedded_file import EmbeddedFile, Metadata
        metadata = Metadata(extension=self.extension, name=self.name, path=self.path)
        return EmbeddedFile(metadata=metadata, document=self.content)
