import os
import requests
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

ENDEE_URL = "http://localhost:8080/api/v1/collections"
COLLECTION_NAME = "study_material"

def create_collection():
    requests.post(ENDEE_URL, json={"name": COLLECTION_NAME})

def load_documents():
    texts = []
    ids = []
    for file in os.listdir("dataset"):
        with open(f"dataset/{file}", "r", encoding="utf-8") as f:
            texts.append(f.read())
            ids.append(file)
    return ids, texts

def ingest_vectors():
    ids, texts = load_documents()

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts).toarray()

    payload = []
    for i in range(len(ids)):
        payload.append({
            "id": ids[i],
            "vector": vectors[i].tolist(),
            "metadata": {"content": texts[i]}
        })

    requests.post(
        f"{ENDEE_URL}/{COLLECTION_NAME}/vectors",
        json={"vectors": payload}
    )

if __name__ == "__main__":
    create_collection()
    ingest_vectors()
    print("✅ Documents ingested into Endee successfully")
