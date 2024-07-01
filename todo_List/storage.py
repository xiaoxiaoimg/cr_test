import json
from task import Task


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return [Task(**task) for task in json.load(file)]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(
            [
                {
                    "title": task.title,
                    "priority": task.priority,
                    "due_date": task.due_date,
                    "category": task.category,
                    "status": task.status,
                }
                for task in tasks
            ],
            file,
        )
