from app.models.task_model import Task

tasks = []

def get_all_tasks():
    return tasks

def create_task(title, description):
    task = Task(len(tasks) + 1, title, description, False)
    tasks.append(task)
    return task