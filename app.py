from flask import Flask, request, jsonify
import os

app = Flask(__name__)

FILE_PATH = os.getenv("FILE_PATH", "./data/notes.txt")

# Ensure directory exists
os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

@app.route("/")
def home():
    return "Notes App Running 🚀"

@app.route("/add", methods=["POST"])
def add_note():
    note = request.json.get("note")

    with open(FILE_PATH, "a") as f:
        f.write(note + "\n")

    return jsonify({"message": "Note added!"})

@app.route("/notes", methods=["GET"])
def get_notes():
    if not os.path.exists(FILE_PATH):
        return jsonify([])

    with open(FILE_PATH, "r") as f:
        notes = f.readlines()

    return jsonify([n.strip() for n in notes])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)