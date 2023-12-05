# job-posting-duplicate-detection

A project aiming to leverage text embeddings and Milvus, a high-performance vector search engine, to detect duplicate job postings. The process involves generating embeddings from job descriptions and utilizing Milvus for efficient duplicate detection.



## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Results and Evaluation](#results-and-evaluation)
- [Docker Integration](#docker-integration)
- [Video Demo](#video-demo)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)



## Introduction

The project focuses on the following key tasks:

1. **Data Preprocessing:** Explore and clean job postings data, handling missing values and anomalies.
2. **Generating Embeddings:** Utilize a pre-trained model (Sentence Transformers) to generate embeddings for job descriptions.
3. **Milvus for Duplicate Detection:** Set up a Milvus instance, insert embeddings, and implement a method to search for potential duplicates.
4. **Docker/Docker Compose Integration:** Containerize the project for easy reproducibility.



## Project Structure

```plaintext
/job-posting-duplicate-detection
|-- data/
|   |-- job_postings.csv
|-- embeddings/
|   |-- generate_embeddings.py
|-- milvus/
|   |-- milvus_setup.py
|   |-- duplicate_detection.py
|-- Dockerfile
|-- docker-compose.yml
|-- video_demo/
|   |-- demo_video.mp4
|-- README.md
```



## Requirements

- Python 3.x
- PyTorch
- Sentence Transformers
- pymilvus

Install dependencies using:

```bash
pip install -r requirements.txt
```



## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/arasgungore/job-posting-duplicate-detection.git
   ```

2. Navigate to the project directory:

   ```bash
   cd job-posting-duplicate-detection
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```



## Usage

1. **Data Preprocessing:**

   Explore and clean the data in the `data/job_postings.csv` file.

2. **Generating Embeddings:**

   Run the following command to generate embeddings:

   ```bash
   python embeddings/generate_embeddings.py
   ```

3. **Milvus for Duplicate Detection:**

   - Set up Milvus instance:

     ```bash
     python milvus/milvus_setup.py
     ```

   - Run duplicate detection:

     ```bash
     python milvus/duplicate_detection.py
     ```

4. **Docker/Docker Compose Integration:**

   - Build and run the Docker image:

     ```bash
     docker build -t job-posting-duplicate-detection .
     docker-compose up
     ```



## Results and Evaluation

Results and evaluation metrics are provided in the code comments of `milvus/duplicate_detection.py`. The effectiveness of the duplicate detection method can be assessed based on precision, recall, and similarity threshold.



## Docker Integration

The project includes Docker and Docker Compose files (`Dockerfile` and `docker-compose.yml`) for containerization. This ensures a reproducible and isolated environment.

To build and run the Docker image, follow the instructions in the [Usage](#usage) section.



## Video Demo

Watch the [demo video](./video_demo/demo_video.mp4) for a quick overview of the project.



## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements or new features.



## License

This project is licensed under the [MIT License](LICENSE).



## Author

👤 **Aras Güngöre**

- LinkedIn: [@arasgungore](https://www.linkedin.com/in/arasgungore)
- GitHub: [@arasgungore](https://github.com/arasgungore)
