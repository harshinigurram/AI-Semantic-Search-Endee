import json
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATASETS = {
    "ai": "dataset/ai_basics.txt",
    "ml": "dataset/ml_notes.txt",
    "dl": "dataset/dl_notes.txt",
    "dbms": "dataset/dbms_notes.txt",
    "web": "dataset/web_dev.txt",
    "java": "dataset/java_notes.txt"
}

def detect_topic(query):
    q = query.lower()

    if "deep learning" in q or "dl" in q:
        return "dl"
    if "machine learning" in q or "ml" in q:
        return "ml"
    if "artificial intelligence" in q or "ai" in q:
        return "ai"
    if "dbms" in q or "database" in q:
        return "dbms"
    if "web" in q or "website" in q:
        return "web"
    if "java" in q:
        return "java"

    return None   # fallback

def semantic_search(query):
    topic = detect_topic(query)

    # If topic detected, use only that file
    files = [DATASETS[topic]] if topic else DATASETS.values()

    answers = []
    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    answers.append(line)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(answers)
    query_vec = vectorizer.transform([query])

    scores = cosine_similarity(query_vec, vectors)[0]

    results = []
    for i, score in enumerate(scores):
        results.append({
            "answer": answers[i],
            "similarity": round(float(score), 3),
            "topic": topic if topic else "mixed"
        })

    results.sort(key=lambda x: x["similarity"], reverse=True)

    save_history(query)
    return results[:5]

def save_history(query):
    try:
        history = json.load(open("search_logs.json"))
    except:
        history = []

    history.append({
        "query": query,
        "time": str(datetime.now())
    })

    json.dump(history, open("search_logs.json", "w"), indent=2)
