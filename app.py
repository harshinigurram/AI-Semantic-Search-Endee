from flask import Flask, request, jsonify, render_template_string
from semantic_query import semantic_search

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>AI Semantic Search</title>
<style>
body {
    font-family: Arial;
    background: #f4f6f8;
    padding: 40px;
}
.container {
    background: white;
    padding: 30px;
    max-width: 900px;
    margin: auto;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}
input {
    width: 70%;
    padding: 10px;
}
button {
    padding: 10px 15px;
}
.result {
    margin-top: 20px;
    padding: 15px;
    background: #eef;
    border-radius: 5px;
}
.score {
    color: green;
    font-weight: bold;
}
img {
    width: 100%;
    margin-top: 20px;
    border-radius: 5px;
}
</style>
</head>

<body>
<div class="container">

<h2>AI Semantic Search using Endee</h2>
<img src="/static/home.png">

<form method="post" action="/search-ui">
<input type="text" name="query" placeholder="Ask about AI, ML, DL, DBMS, Web, Java..." required>
<button type="submit">Search</button>
</form>

{% if results %}
<h3>Relevant Answers:</h3>
{% for r in results %}
<div class="result">
<p>{{ r.answer }}</p>
<p class="score">Similarity Score: {{ r.similarity }}</p>
</div>
{% endfor %}
<img src="/static/search.png">
{% endif %}

</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/search-ui", methods=["POST"])
def search_ui():
    query = request.form["query"]
    results = semantic_search(query)
    return render_template_string(HTML, results=results)

@app.route("/search", methods=["POST"])
def search_api():
    return jsonify(semantic_search(request.json["query"]))

if __name__ == "__main__":
    app.run(debug=True)
