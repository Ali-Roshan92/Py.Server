from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, From Zandian!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionary to store received data
data_store = {}

@app.route('/', methods=['GET'])
def home():
    # This route responds with a simple message
    return "Hello, Render!"

@app.route('/data', methods=['POST'])
def receive_data():
    # This route handles POST requests to receive data
    # Getting the JSON data from the POST request
    data = request.json  # Assumes data is sent in JSON format
    # Store the received data in the data_store dictionary
    data_store.update(data)
    return jsonify({"message": "Data received!", "data": data}), 201  # Respond with a message and the received data

@app.route('/data', methods=['GET'])
def get_data():
    # This route handles GET requests to retrieve stored data
    return jsonify(data_store), 200  # Return the data_store dictionary as JSON

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)  # Make the server accessible from any address
