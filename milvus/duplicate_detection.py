# Import necessary libraries
from pymilvus import connections, utility

# Set up Milvus connection
connections.connect()

# Define similarity threshold
similarity_threshold = 0.9

# Load embeddings from file
embedding_file_path = "../embeddings/job_description_embeddings.pt"
embeddings = torch.load(embedding_file_path)

# Insert embeddings into Milvus
collection_name = "job_posting_collection"
utility.insert(collection_name, embeddings)

# Search for potential duplicates
def search_duplicates(query_embedding):
    result = utility.search(collection_name, query_embedding, similarity_threshold)
    return result

# Example usage
query_embedding = model.encode("Sample job description", convert_to_tensor=True)
duplicates = search_duplicates(query_embedding)
print("Potential Duplicates:", duplicates)
