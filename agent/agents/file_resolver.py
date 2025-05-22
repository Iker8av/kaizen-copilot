import re
from typing import Tuple, Union
from agent.models.agentbase import AgentBase
from agent.models.context import Context
from agent.models.input import  FileInput
from agent.models.mcpstep import ROLE
from agent.models.output import FileBaseOutput, QueryFormatterOutput
from agent.tools.chromadb import ChromaDB
from agent.tools.tool import Tool

class FileResolver(AgentBase[FileInput, Union[FileBaseOutput, QueryFormatterOutput]]):
    def __init__(self):
        self.aget_name: str = "FileResolver"
        self.role: ROLE = ROLE.FILE_RESOLVER
        self.tool: Tool = ChromaDB()
        self.purpose: str = "Ensure LLM Model will have enough context, if not, it wil iterate with the Vector DB"
    
    def run(self, _, context: Context) -> Tuple[Union[FileBaseOutput, QueryFormatterOutput], Context, int]:
        self.context = context
        
        if len(context.retrieved_files) > 1:
            return FileBaseOutput(self.context.retrieved_files), self.context, 1
        else:
            main_file = context.retrieved_files[0]
            extension = main_file.extension
            code = main_file.content
            
            queries: list[str] = []
            if extension == "py":
                from_imports: list[str] = re.findall(r'^\s*from\s+[a-zA-Z_][\w\.]*\s+import\s+[a-zA-Z_][\w]*', code, re.MULTILINE)
                unique_paths = []
                
                if len(from_imports) <= 0:
                    return FileBaseOutput(self.context.retrieved_files), self.context, 1
                
                for include in from_imports:
                    tokens = include.lstrip().split(" ")
                    dependencies_name = tokens[1]
                    relative_path = dependencies_name.replace(".","/")
                    imports_names = tokens[-1].split(",")
                    class_names = []
                    function_names = []
                    constants_names = []
                    
                    for import_name in imports_names:
                        if import_name[0].isupper() and import_name[1].islower():
                            class_query = f"""class {import_name}\n\tdef __init__("""
                            class_names.append(class_query)
                        elif import_name.isupper():
                            constant_query = f"{import_name} ="
                            constants_names.append(constant_query)
                        else:
                            function_query = f"def {import_name}("
                            function_names.append(function_query)
                            
                    imports_file_code = "\n".join(class_names) + "\n" + "\n".join(constants_names) + "\n" + "\n".join(function_names)
                    query = f"{relative_path}.py\n\n{imports_file_code}".strip()
                    
                    if relative_path in unique_paths:
                        index = next((i for i, path in enumerate(unique_paths) if relative_path in path), -1)
                        old_query = queries[index]
                        new_query: str = old_query + "\n\n" + imports_file_code 
                        queries[index] = new_query.strip()
                        continue
                    
                    print(query)
                    unique_paths.append(relative_path)
                    queries.append(query)
                
            elif extension == "c" or extension == "cpp":
                includes: list[str] = re.findall(r'^\s*#include\s+["].+["]', code, re.MULTILINE)
                
                if len(includes) <= 0:
                    return FileBaseOutput(self.context.retrieved_files), self.context, 1
                
                for include in includes:
                    dependencies_name = include.lstrip().replace('"', "").split(" ")[1]
                    class_name = dependencies_name.split(".")[0]
                    
                    query = f"/{dependencies_name}\n#ifndef {class_name.upper()}_H\n#define {class_name.upper()}_H\nclass {class_name} "+"{"+"\npublic:\nclass file"
                    
                    queries.append(query) 
                    
            elif extension == "java":
                imports: list[str] = re.findall(r'^\s*import\s+(?!java|javax).', code, re.MULTILINE)
                
                if len(imports) <= 0:
                    return FileBaseOutput(self.context.retrieved_files), self.context, 1
                
                for import_line in imports:
                    dependencies_name = import_line[:-1].split(" ")[-1]
                    relative_path = dependencies_name.replace(".", "/")
                    class_name = dependencies_name.split(".")[-1]
                    package_name = dependencies_name.split(".")[0]
                    query = f"/{relative_path} package {package_name};\npublic class {class_name} " + "{" 
                    queries.append(query) 
                    
                
            return QueryFormatterOutput(queries=queries, metadata=None), self.context, -1