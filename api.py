from flask import Flask, request, jsonify
from agent.models.mcphost import MCPHost
from agent.models.issue import Issue
from agent.models.input import QueryFormatterInput

app = Flask(__name__)

app.config['DEBUG'] = True
    
@app.route('/fix_issue', methods=['GET'])
def fix_issue():
    if request.method =='GET':
        issue = Issue()
        issue.title = request.args.get('title')
        issue.description = request.args.get('description')
        issue.repo_url = request.args.get('repo_url')

        input_data = QueryFormatterInput(issue)
        host = MCPHost()
       
        solution = host.run_workflow('issue_resolution', input_data)

        return jsonify(solution, status=200)


if __name__ == '__main__':
    app.run()