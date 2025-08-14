from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory data
data = [
    {"id": 1, "name": "Apple"},
    {"id": 2, "name": "Banana"}
]

# GET all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

# GET single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item["id"] == item_id), None)
    return jsonify(item) if item else ("Item not found", 404)

# POST add new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    new_item["id"] = len(data) + 1
    data.append(new_item)
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(debug=True)
