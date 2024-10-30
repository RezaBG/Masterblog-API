from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route("/")
def home():
    return "Welcome to the Masterblog API"

@app.route('/api/posts', methods=['GET'])
def get_posts():
    """
    Endpoint to retrieve all posts.
    Returns a json array of all posts.
    """
    return jsonify(POSTS), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
