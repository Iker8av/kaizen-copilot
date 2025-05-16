from dataclasses import dataclass
from uuid import UUID


@dataclass
class Issue():
    id: UUID
    title: str
    description: str
    repo_url: str
    
    def fetch_repo(self) -> None:
        pass
    