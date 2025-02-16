from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_task():
    task_description = request.args.get('task')
    if not task_description:
        return jsonify({"error": "No task provided"}), 400
    try:
        result = execute_task(task_description)
        return jsonify({"status": "success", "output": result}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

@app.route('/read', methods=['GET'])
def read_file():
    file_path = request.args.get('path')
    if not file_path or not file_path.startswith("/data/"):
        return jsonify({"error": "Invalid file path"}), 400
    if not os.path.exists(file_path):
        return "", 404
    with open(file_path, "r") as file:
        return file.read(), 200

def execute_task(task_description):
    # TODO: Implement the logic to handle various tasks
    return f"Task '{task_description}' executed."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
