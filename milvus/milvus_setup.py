# Import necessary libraries
from pymilvus import connections, FieldSchema, CollectionSchema, DataType

# Set up Milvus connection
connections.connect()

# Define Milvus collection and fields
collection_name = "job_posting_collection"
fields = [FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=768)]
schema = CollectionSchema(fields=fields, description="Collection for job posting embeddings")

# Create collection
collection = connections.create_collection(schema, collection_name)
