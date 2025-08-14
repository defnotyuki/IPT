from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)

# Data storage
data = [
    {"id": 1, "name": "Apple"},
    {"id": 2, "name": "Banana"}
]
deleted_items = []

@app.route('/')
def home():
    return "Welcome to the API! Go to /add to view, add, delete, restore, or edit data."

@app.route('/add', methods=['GET', 'POST'])
def add_form():
    global data, deleted_items

    if request.method == 'POST':
        action = request.form.get("action")

        if action == "add":
            name = request.form['name']
            new_item = {"id": len(data) + 1, "name": name}
            data.append(new_item)

        elif action == "delete":
            item_id = int(request.form['id'])
            item_to_delete = next((item for item in data if item["id"] == item_id), None)
            if item_to_delete:
                data = [item for item in data if item["id"] != item_id]
                deleted_items.append(item_to_delete)
                for idx, item in enumerate(data, start=1):
                    item["id"] = idx

        elif action == "restore":
            item_id = int(request.form['id'])
            item_to_restore = next((item for item in deleted_items if item["id"] == item_id), None)
            if item_to_restore:
                deleted_items = [item for item in deleted_items if item["id"] != item_id]
                data.append({"id": len(data) + 1, "name": item_to_restore["name"]})

        elif action == "edit":
            item_id = int(request.form['id'])
            new_name = request.form['name']
            for item in data:
                if item["id"] == item_id:
                    item["name"] = new_name
                    break

    html_page = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Item Manager</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <div class="container py-4">
            <h1 class="text-center mb-4">Item Manager</h1>

            <!-- Add Item Form -->
            <div class="card mb-4 shadow-sm">
                <div class="card-header bg-primary text-white">Add New Item</div>
                <div class="card-body">
                    <form method="POST" class="row g-2">
                        <input type="hidden" name="action" value="add">
                        <div class="col-auto">
                            <input type="text" class="form-control" name="name" placeholder="Enter item name" required>
                        </div>
                        <div class="col-auto">
                            <button type="submit" class="btn btn-success">Add</button>
                        </div>
                    </form>
                </div>
            </div>

            <!-- Current Items -->
            <div class="card mb-4 shadow-sm">
                <div class="card-header bg-success text-white">Current Items</div>
                <div class="card-body">
                    {% if items %}
                        <table class="table table-bordered table-striped">
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th style="width: 250px;">Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for item in items %}
                                    <tr>
                                        <td>{{ item.id }}</td>
                                        <td>
                                            <form method="POST" class="d-flex">
                                                <input type="hidden" name="action" value="edit">
                                                <input type="hidden" name="id" value="{{ item.id }}">
                                                <input type="text" name="name" value="{{ item.name }}" class="form-control me-2" required>
                                                <button class="btn btn-warning btn-sm me-1">Edit</button>
                                            </form>
                                        </td>
                                        <td>
                                            <form method="POST" style="display:inline;">
                                                <input type="hidden" name="action" value="delete">
                                                <input type="hidden" name="id" value="{{ item.id }}">
                                                <button class="btn btn-danger btn-sm">Delete</button>
                                            </form>
                                        </td>
                                    </tr>
                                {% endfor %}
                            </tbody>
                        </table>
                    {% else %}
                        <p class="text-muted">No active items.</p>
                    {% endif %}
                </div>
            </div>

            <!-- Deleted Items -->
            <div class="card shadow-sm">
                <div class="card-header bg-secondary text-white">Deleted Items</div>
                <div class="card-body">
                    {% if deleted %}
                        <table class="table table-bordered table-striped">
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th style="width: 150px;">Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for item in deleted %}
                                    <tr>
                                        <td>{{ item.id }}</td>
                                        <td>{{ item.name }}</td>
                                        <td>
                                            <form method="POST" style="display:inline;">
                                                <input type="hidden" name="action" value="restore">
                                                <input type="hidden" name="id" value="{{ item.id }}">
                                                <button class="btn btn-info btn-sm">Restore</button>
                                            </form>
                                        </td>
                                    </tr>
                                {% endfor %}
                            </tbody>
                        </table>
                    {% else %}
                        <p class="text-muted">No deleted items.</p>
                    {% endif %}
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_page, items=data, deleted=deleted_items)

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

@app.route('/deleted_items', methods=['GET'])
def get_deleted_items():
    return jsonify(deleted_items)

if __name__ == '__main__':
    app.run(debug=True)
