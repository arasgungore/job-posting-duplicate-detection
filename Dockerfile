# Use an official PyTorch runtime as a parent image
FROM pytorch/pytorch:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Define environment variable
ENV NAME job_posting_duplicate_detection

# Run generate_embeddings.py when the container launches
CMD ["python", "./embeddings/generate_embeddings.py"]
