from flask import Flask,  jsonify, request
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]



app = Flask(__name__)
@app.route('/todos', methods=['GET'])
def hello_world():
    my_json = jsonify(todos)
    return my_json

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body) #
    response_body = todos
    return response_body

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    response_body = todos
    return response_body

# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
