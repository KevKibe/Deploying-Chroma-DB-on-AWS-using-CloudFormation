import os
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions 
from dotenv import load_dotenv
load_dotenv()
#create an .env file to store your api key or just assign the variable openai_api_key to your key
openai_api_key = os.getenv('OPENAI_API_KEY')
print("Imported necessary modules.")

chroma_client = chromadb.HttpClient(host="51.20.63.152", port = 8000)

print("Created ChromaDB client.")

documents=[
            "Artificial Intelligence (AI) refers to the simulation of human intelligence processes by machines, especially computer systems. These processes include learning (the acquisition of information and rules for using the information), reasoning (using rules to reach approximate or definite conclusions) and self-correction.",
            "Space exploration is the discovery and exploration of celestial structures in outer space by means of evolving and growing space technology. While the study of space is carried out mainly by astronomers with telescopes, its physical exploration though is conducted both by unmanned robotic space probes and human spaceflight.",
            "Climate change is a significant and lasting change in the statistical distribution of weather patterns over periods ranging from decades to millions of years. It may be a change in average weather conditions, or in the distribution of weather around the average conditions. This phenomenon has been linked to the increase in greenhouse gases in our atmosphere, leading to warmer temperatures on earth."
          ]

print("Defined documents.")

collection_status = False
while not collection_status:
    try:
        document_collection = chroma_client.get_or_create_collection(name="random_collection_01")
        collection_status = True
        print("Collection 'random_collection_01' created.")
    except Exception as e:
        print("Failed to create collection. Retrying...")

if collection_status:
    metadatas = [{'source': "Artificial Intelligence"}, {'source': "Space Exploration"}, {'source': "Climate Change"}]
    ids = ["1", "2", "3"]
    openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                api_key=openai_api_key,
                model_name="text-embedding-ada-002"
            )

    embeddings = [openai_ef(doc) for doc in documents]
    document_collection.add(documents=documents, metadatas=metadatas, ids=ids, embeddings= embeddings)

    print("Added documents to the collection.")

