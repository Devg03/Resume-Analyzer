from flask import Flask, request, jsonify
from flask_cors import CORS
from pdfminer.high_level import extract_text
import tempfile

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

@app.route('/api/parse-resume', methods = ['POST'])
def parse_resume():
    if 'resume' not in request.files:
        return jsonify({"error": "No File Uploaded"}), 400
    
    file = request.files["resume"]
    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    if not file.filename.endswith(".pdf"):
        return jsonify({"error": "File must be a PDF"}), 400

    

if __name__ == "__main__":
    app.run(debug=True, port=5000)
