from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionary to store received data
data_store = {}

@app.route('/', methods=['GET'])
def home():
    return "Hello, This is Test Server!"

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json  # Get JSON data from the request
    data_store.update(data)  # Store received data
    return jsonify({"message": "Data received!", "data": data}), 201  # Response

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_store), 200  # Return stored data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
