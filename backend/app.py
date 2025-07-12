from flask import Flask, request, jsonify
from flask_cors import CORS
import fitz

app = Flask(__name__)
CORS(app, origins="http://localhost:5173", supports_credentials=True)

@app.route('/api/parse-resume', methods = ['POST'])
def parse_resume():
    if 'resume' not in request.files:
        return jsonify({"error", "No File Uploaded"}), 400
    
    file = request.files["resume"]
    if file.filename == "":
        return jsonify({"error", "Empty filename"}), 400
    
    # Potential error here
    if not file.endswith('.pdf'):
        return jsonify({"error", "Invalid file extension"}), 400

    

if __name__ == "__main__":
    app.run(debug=True, port=5000)