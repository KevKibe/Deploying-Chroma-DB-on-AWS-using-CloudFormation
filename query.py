import os
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions 
from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
chroma_client = chromadb.HttpClient(host="51.20.63.152", port = 8000)
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                api_key=openai_api_key,
                model_name="text-embedding-ada-002"
            )

document_collection = chroma_client.get_collection(name="random_collection_01")

results = document_collection.query(query_texts="tell me about space", n_results=1, embeddings=openai_ef)
result_documents = results["documents"][0]

for doc in result_documents:
    print(doc["text"])
