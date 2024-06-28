from task import Task
from storage import load_tasks, save_tasks
import sys


class TodoList:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, title, priority, due_date, category):
        new_task = Task(title, priority, due_date, category, "pending")
        self.tasks.append(new_task)
        save_tasks(self.tasks)

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            save_tasks(self.tasks)
        else:
            sys.exit("任务不存在")

    def sort_tasks(self):
        assert len(self.tasks) > 0, "任务列表为空"
        self.tasks.sort(key=lambda x: x.due_date)
