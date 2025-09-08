from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage (for demo purposes only)
users = []
help_requests = []

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    users.append(data)
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/post_help_request', methods=['POST'])
def post_help_request():
    data = request.json
    help_requests.append(data)
    return jsonify({'message': 'Help request posted'}), 201

@app.route('/get_help_requests', methods=['GET'])
def get_help_requests():
    return jsonify(help_requests), 200

@app.route('/connect', methods=['POST'])
def connect():
    data = request.json
    # Add logic for connecting a helper with a request
    return jsonify({'message': 'Connection established!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
