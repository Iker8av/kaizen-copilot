from agent.models.issue import Issue
from agent.models.mcplog import MCPLog
from agent.models.mcpstep import MCPStep
from agent.models.output import FileBaseOutput


class MCPHost:
    def __init__(self):
        self.mcp_log = MCPLog()
        self.agents: dict[str, str] = {
            # Define Agents
        }
        self.tools = dict[str, str] = {
            
        }
        
        
        pass
    
    def fix_issue(self, issue: Issue) -> None:
        pass
    
    def on_installed(self, repo: FileBaseOutput) -> None:
        pass
    
    def _log_step(self, step: MCPStep) -> None:
        pass