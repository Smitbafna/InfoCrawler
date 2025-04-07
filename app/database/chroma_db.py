import chromadb

client = chromadb.Client()
collection = client.get_collection("support_docs")

def add_documents_to_db(documents):
    collection.add_documents(documents)
    
def retrieve_context(query):
    results = collection.query(query_texts=[query], n_results=3)
    return results['documents'][0]
