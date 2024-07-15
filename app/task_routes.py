from flask import Blueprint, jsonify, request
from app.controllers.task_controller import get_all_tasks, create_task

task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = get_all_tasks()
    return jsonify([task.__dict__ for task in tasks])

@task_bp.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    new_task = create_task(title, description)
    return jsonify(new_task.__dict__), 201