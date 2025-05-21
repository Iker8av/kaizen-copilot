from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/fix_issue', methods=['GET'])
def fix_issue():
    if request.method =='GET':
        text = request.get_json()
        return text
    

if __name__ == '__main__':
    app.run(debug=True)