AI Semantic Search using Endee Vector Database

Project Overview
This project implements an **AI-powered Semantic Search system** using **Endee** as the vector database.
Unlike traditional keyword-based search, semantic search retrieves information based on **meaning and context**.

The system allows users to ask questions related to multiple domains such as:
- Artificial Intelligence
- Machine Learning
- Deep Learning
- DBMS
- Web Development
- Java

and returns the most **semantically relevant answers** along with similarity scores.

Problem Statement
Traditional keyword-based search systems fail to capture the semantic meaning of user queries.
As a result, they often return irrelevant or incomplete results.

This project addresses the problem by:
- Representing text as vector embeddings
- Comparing queries and documents using similarity measures
- Retrieving conceptually relevant answers instead of exact keyword matches

 🏗️ System Design / Technical Approach

 1️.Data Collection
- Domain-specific knowledge is stored as plain text files inside the `dataset/` folder
- Each file contains **multiple answers per topic**

2. Vectorization
- Text data is converted into numerical representations using **TF-IDF vectorization**
- This approach works completely **offline** and does not depend on external APIs

3.Vector Storage (Endee)
- Generated vectors are ingested into **Endee**, which acts as the vector database
- Endee is responsible for managing and organizing vector data efficiently

4. Query Processing
- User input is analyzed to detect the topic (AI, ML, DL, DBMS, etc.)
- The query is vectorized using the same TF-IDF model

5.Similarity Computation
- **Cosine similarity** is used to compare the query vector with stored document vectors
- Results are ranked based on similarity score

6. Result Presentation
- Top relevant answers are displayed in a simple web interface
- Each answer includes a similarity score for interpretability



 -->How Endee Is Used in This Project
Endee is used as the **vector database layer** in the system architecture.

- Document embeddings are stored in Endee collections
- Endee simulates real-world vector database usage for semantic retrieval
- The project architecture follows industry-standard AI pipelines where:
  - Embeddings are generated
  - Vectors are stored in a vector DB
  - Queries are matched using vector similarity

This demonstrates how Endee can be integrated into AI/ML applications such as:
- Semantic Search
- Retrieval-Augmented Generation (RAG)
- Recommendation Systems



 --->Application Screenshots

Home Page
![Home Page](static/home.png)

 Semantic Search Results
![Search Result](static/search.png)



 Setup and Execution Instructions

1. Prerequisites
Ensure the following are installed:
- Python 3.9 or above
- Docker Desktop
- Git


2.Start Endee Vector Database
Make sure Docker Desktop is running, then execute:
bash
docker run -p 8080:8080 endeeio/endee-server:latest
