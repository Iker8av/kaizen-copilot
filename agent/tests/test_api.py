from flask import Flask, request
import chromadb
from sentence_transformers import SentenceTransformer
import os

chorma_client = None
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/test_args', methods=['GET'])
def test_args():
    if request.method =='GET':
        text = request.get_json()
        return text
    
@app.route('/db/save_in_collection', methods=['POST'])
def save_in_collection():
    if request.method =='POST':
        data = request.get_json()
        collection = chroma_client.get_or_create_collection(name=data["collection"])
        
        files_list = data["files_list"]
        docs = []
        embedds = []
        
        for file_name in files_list:
            file_path = os.path.abspath(f"./agent/tests/sample_files/{file_name}")
            
            with open(file_path, "r", encoding="utf-8") as f:
                file_content = f.read()

            # Prepare text to embed (file name + content)
            text_to_embed = f"{file_path} {file_content}"
            docs.append(text_to_embed)

            embedds.append(embedder.encode([text_to_embed])[0].tolist())
            
        collection.upsert(
            ids=[f"{index}_{file_name}" for index, file_name in enumerate(files_list)],  # unique ID
            documents=docs,
            embeddings=embedds,
            metadatas=[{"file_name": files_list[i]} for i in range(len(docs))]
        )
        
        return "OK", 200
    
@app.route('/db/query', methods=['GET'])
def query():
    if request.method =='GET':
        data = request.get_json()
        
        collection = chroma_client.get_or_create_collection(name=data["collection"])
        
        results = collection.query(
            query_texts=[data["query"]], 
            n_results=1 
        )
        return results

if __name__ == '__main__':
    chroma_client = chromadb.HttpClient(host="localhost", port=8005)
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    app.run(debug=True)