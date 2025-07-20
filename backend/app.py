from flask import Flask, request, jsonify
from flask_cors import CORS
import fitz

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

@app.route('/api/parse-resume', methods = ['POST'])
def parse_resume():
    text = "Succesfully Grabbed"
    return jsonify(text)

if __name__ == "__main__":
    app.run(debug=True, port=5000)