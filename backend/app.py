from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="http://localhost:5173", supports_credentials=True)

@app.route('/api/parse-resume', methods = ['POST'])
def parse_resume():
    pass

if __name__ == "__main__":
    app.run(debug=True, port=5000)