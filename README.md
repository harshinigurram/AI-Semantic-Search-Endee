---

## 🧠 Key Features Implemented
- Semantic (meaning-based) search instead of keyword matching  
- Multiple answers supported for a single topic (AI, ML, DL, DBMS, Web Development, Java)  
- Topic-aware search to avoid cross-domain confusion  
- Similarity score calculation using cosine similarity  
- Ranked search results based on relevance  
- Offline vector generation using TF-IDF (no external API dependency)  
- Clean and simple web interface for interaction  

---

## 🧩 How Endee Is Used in This Project
Endee is used as the **vector database layer** in this project.

- Document embeddings are generated from text files  
- These embeddings are ingested into Endee collections  
- Endee is responsible for storing and managing vector data efficiently  
- The system design follows real-world AI architectures where a vector database
  is used for scalable semantic retrieval  

Although similarity computation is handled locally for stability, Endee remains
the central vector storage component in the system design.

---

## 🧪 Example Queries
You can test the system using queries such as:
- *What is Artificial Intelligence?*  
- *Explain Machine Learning*  
- *What is Deep Learning?*  
- *What is DBMS?*  
- *Explain Web Development*  
- *What is Java?*  

Each query returns:
- Multiple relevant answers  
- A similarity score for each answer  
- Results sorted by relevance  

---

## ⚙️ Detailed Setup Instructions

### 1️⃣ Prerequisites
- Python 3.9 or higher  
- Docker Desktop  
- Git  

---

### 2️⃣ Start Endee Vector Database
Ensure Docker Desktop is running, then start the Endee server:
```bash
docker run -p 8080:8080 endeeio/endee-server:latest
