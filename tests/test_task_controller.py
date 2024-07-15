from app.controllers.task_controller import get_all_tasks, create_task

def test_get_all_tasks():
    tasks = get_all_tasks()
    assert tasks == []

def test_create_task():
    new_task = create_task('Task 1', 'Description of Task 1')
    assert new_task.id == 1
    assert new_task.title == 'Task 1'
    assert new_task.description == 'Description of Task 1'
    assert new_task.completed == False