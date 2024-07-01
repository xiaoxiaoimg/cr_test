class Task:
    def __init__(self, title, priority, due_date, category, status):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.category = category
        self.status = status

    def edit(self, title=None, priority=None, due_date=None, category=None, status=None):
        assert self.status != "completed", "不能编辑已完成的任务"
        if title:
            self.title = title
        if priority:
            self.priority = priority
        if due_date:
            self.due_date = due_date
        if category:
            self.category = category
        if status:
            self.status = status

    def __repr__(self):
        return f"{self.title} ({self.priority})"
