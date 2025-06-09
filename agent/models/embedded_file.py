
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from uuid import UUID, uuid4
from agent.models.file import FILE_TYPE
from agent.models.context import Context

from chromadb import QueryResult

@dataclass
class EmbeddedFile():
    document: str
    metadata: "Metadata"
    embeddings: List[float] = field(default_factory=list)
    id: UUID = field(default_factory=uuid4)
    
    def convert_to_file_class(self, context: Context) -> "File": # type: ignore
        from agent.models.file import File
        code = self.document.replace("[CLS]", "")
        file_type = FILE_TYPE.MAIN_FILE if len(context.retrieved_files) == 0 else FILE_TYPE.DEPENDENCY
        return File(name=self.metadata.name, path=self.metadata.path, content=code, extension=self.metadata.extension, file_type=file_type)
    
    @classmethod
    def convert_query_result_to_embedding(cls, result: QueryResult) -> "EmbeddedFile":
        query_metadata = result["metadatas"][0][0]
        metadata = Metadata(extension=query_metadata["extension"], name=query_metadata["name"], path=query_metadata["path"])
        return cls(metadata=metadata, document=result["documents"][0][0], embeddings=result["embeddings"][0], id=result["ids"][0])
        
    
class Metadata():
    def __init__(self, extension: Optional[str], name: Optional[str] = "", path: Optional[str] = ""):
        self.extension: str = extension
        self.name: str = name
        self.path: str = path
        pass