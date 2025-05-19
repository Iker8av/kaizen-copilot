from typing import List
from chromadb import chromadb, QueryResult
from agent.models.context import Context
from agent.models.embedded_file import EmbeddedFile, Metadata
from agent.tools.tool import Tool


class ChromaDB(Tool):
    def __init__(self):
        super().__init__()
        self.chroma_client = chromadb.HttpClient(host="localhost", port=8005)
        self.collection = None
        
    def execute(self, workflow, inputs: List[EmbeddedFile], context: Context) -> List[EmbeddedFile]:
        #! SET COLLECTION NAMING RULE
        self.collection = self.chroma_client.get_collection(name="code_files") 
        
        if workflow == "issue_resolution":
            return self.query_chroma(inputs)
        pass
        
    def query_chroma(self, embedding_files: List[EmbeddedFile]) -> List[EmbeddedFile]:
        results = []
        for embedding_file in embedding_files:
            results.append(self.collection.query(
                query_embeddings=embedding_file.embeddings, 
                # where={"extension": embedding_file.metadata.extension},
                n_results=1 ,
                include=["documents", "metadatas", "embeddings"]
            ))
        new_embedding_files = self.convert_many_query_results(results)
        return new_embedding_files
    
    def convert_many_query_results(self, results: List[QueryResult]) -> List[EmbeddedFile]:
        all_files = []
        for r in results:
            embedding_file = EmbeddedFile.convert_query_result_to_embedding(r)
            all_files.append(embedding_file)
        return all_files
    