from dataclasses import dataclass
from uuid import UUID


@dataclass
class Issue():
    title: str
    description: str
    repo_url: str
    repo_name: str
    
    def __init__(self, title: str, description: str, repo_url: str):
        self.title = title
        self.description = description
        self.repo_url = repo_url
        self.repo_name = "/".join(repo_url.split("/")[-2:])
        pass