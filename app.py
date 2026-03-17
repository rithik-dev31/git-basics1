from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import uuid
from datetime import datetime

app = Flask(__name__)
CORS(app)

# In-memory storage for tasks (in production, use a database)
tasks = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({'error': 'Task text is required'}), 400
    
    task = {
        'id': str(uuid.uuid4()),
        'text': data['text'],
        'completed': False,
        'created_at': datetime.now().isoformat()
    }
    
    tasks.append(task)
    return jsonify(task), 201

@app.route('/api/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task by ID"""
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    
    return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
