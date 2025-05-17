from enum import Enum
import re
from typing import Optional

from agent.models.agentbase import AgentBase
from agent.models.context import Context
from agent.models.embedded_file import EmbeddedFile, Metadata
from agent.models.input import InputBase, QueryFormatterInput
from agent.models.mcpstep import ROLE, MCPStep
from agent.models.output import OutputBase, QueryFormatterOutput

"""
Query formart according to how the files are recorded:
"""

class CodeExtension(Enum):
    python = "py"
    cpp = "cpp"
    csharp = "csharp"
    java = "java"
    javascript = "js"
    typescript = "ts"
    html = "html"
    css = "css"
    json = "json"
    bash = "sh"
    shell = "sh"
    ruby = "rb"
    go = "go"
    rust = "rs"
    php = "php"
    kotlin = "kt"
    swift = "swift"
    sql = "sql"
    yaml = "yaml"
    markdown = "md"

def get_extension(language: str) -> Optional[str]:
    try:
        return CodeExtension[language.lower()].value
    except KeyError:
        return None
    
class QueryFormatter(AgentBase[QueryFormatterInput, QueryFormatterOutput]):
    def __init__(self):
        self.aget_name: str = "QueryFormatter"
        self.agent_input: InputBase = None
        self.output: OutputBase = None
        self.role: ROLE = ROLE.QUERY_FORMATTER
        self.context: Context = None
        self.purpose: str = "Format the issue to solve to create a properly query to find the files"
        self.step: Optional[MCPStep] = None
        pass
    
    def run(self, input_data: QueryFormatterInput) -> QueryFormatterOutput:
        issue_description = input_data.issue.description
        
        match = re.search(r"```(\w+)?\n(.*?)```", issue_description, re.DOTALL)


        if match:
            language = match.group(1)
            extension = get_extension(language)
            code = match.group(2)
            
            start, end = match.span()  
            outside_text = (issue_description[:start] + issue_description[end:]).strip()  
            
            final_string = f"{extension}\n{outside_text}\n{code}"
            
            metadata = Metadata(extension=extension)
            
            return EmbeddedFile(document=final_string, metadata=metadata)
        else:
            raise Exception("No match found")
        
        pass
