from typing import Tuple
from sentence_transformers import SentenceTransformer

from agent.models.agentbase import AgentBase
from agent.models.context import Context
from agent.models.input import EmbeddedFileInput
from agent.models.mcpstep import ROLE
from agent.models.output import EmbeddedFileOutput
from agent.tools.chromadb import ChromaDB
from agent.tools.tool import Tool


class EmbeddingModel(AgentBase[EmbeddedFileInput, EmbeddedFileOutput]):
    def __init__(self):
        self.aget_name: str = "EmbeddingModel"
        self.role: ROLE = ROLE.EMBEDDING
        self.tool: Tool = ChromaDB()
        self.purpose: str = "Creates Embedding of the files to story or query in the vector database"
        
        self.__model = SentenceTransformer('all-MiniLM-L6-v2')
        pass
    
    def run(self, input_data: EmbeddedFileInput, context: Context) -> Tuple[EmbeddedFileOutput, Context]:
        self.context = context
        embedded_files = input_data.embedded_files
        
        for embedded_file in embedded_files:           
            embedding = self.__model.encode(embedded_file.document)
            embedded_file.embeddings = embedding.tolist()   
            
        results = self.tool.execute(workflow=context.workflow, inputs=embedded_files, context=context)      
                    
        return EmbeddedFileOutput(results), self.context, 1
