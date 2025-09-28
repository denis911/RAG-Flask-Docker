
from flask import Flask, request, jsonify
# import requests 
from minsearch import AppendableIndex
from search_tools import SearchTools
from toyaikit.tools import wrap_instance_methods
import json
import os


def init_index():
    # docs_url = 'https://github.com/alexeygrigorev/llm-rag-workshop/raw/main/notebooks/documents.json'
    # docs_response = requests.get(docs_url)
    # documents_raw = docs_response.json()

    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    documents_path = os.path.join(script_dir, "documents.json")
    with open(documents_path, "r", encoding="utf-8") as f:
        documents_raw = json.load(f)

    documents = []

    for course in documents_raw:
        course_name = course['course']

        for doc in course['documents']:
            doc['course'] = course_name
            documents.append(doc)

    # print(documents[1]) # uncomment to see documents format

    index = AppendableIndex(
        text_fields=["question", "text", "section"],
        keyword_fields=["course"]
    )

    index.fit(documents)
    return index


def init_tools():
    index = init_index()
    return SearchTools(index)

# Initialize Flask and tools
app = Flask(__name__)
tools = init_tools()


@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")

    if not query:
        return jsonify({"error": "Missing query parameter 'q'"}), 400

    results = tools.search(query=query)
    return jsonify(results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


