from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="http://localhost:5173", supports_credentials=True)

@app.route('/api/parse-resume', methods = ['POST'])
def parse_resume():
    if request.method == 'OPTIONS':
            # Preflight request
            return '', 200

    data = request.get_json()
    name = data.get('name', 'Unknown')
    return jsonify({
        'message': f'Resume parsed for {name}',
        'success': True
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)