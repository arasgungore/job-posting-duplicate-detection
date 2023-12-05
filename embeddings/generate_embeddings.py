# Import necessary libraries
import pandas as pd
from sentence_transformers import SentenceTransformer
import os

# Load data
data_path = "../data/jobpostings.csv"
df = pd.read_csv(data_path)

# Load pre-trained Sentence Transformer model
model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

# Generate embeddings and save to file
embeddings = model.encode(df['Job Description'].tolist(), convert_to_tensor=True)
embedding_file_path = "../embeddings/job_description_embeddings.pt"
torch.save(embeddings, embedding_file_path)
