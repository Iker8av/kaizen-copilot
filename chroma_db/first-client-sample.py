# import asyncio
# import chromadb
# # Example setup of the client to connect to your chroma server
# client = chromadb.HttpClient(host='localhost', port=8000)

# async def main():           
#     collection = await client.create_collection(name="my_collection")
#     await collection.add(
#         documents=["hello world"],
#         ids=["id1"]
#     )

# asyncio.run(main())

from chromadb import HttpClient
from chromadb.config import Settings
settings = Settings(chroma_api_impl="chromadb.api.fastapi.FastAPI")
chroma_client = HttpClient(host="localhost", port=8005, settings=settings)

# switch `create_collection` to `get_or_create_collection` to avoid creating a new collection every time
collection = chroma_client.get_or_create_collection(name="my_collection")

# switch `add` to `upsert` to avoid adding the same documents every time
collection.upsert(
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges"
    ],
    ids=["id1", "id2"]
)

results = collection.query(
    query_texts=["This is a query document about florida"], # Chroma will embed this for you
    n_results=2 # how many results to return
)

print(results)
