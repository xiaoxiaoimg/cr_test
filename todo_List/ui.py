from todo_list import TodoList
from task import Task
import sys


def log_error(message):
    print(f"Error: {message}")


def display_menu(todo_list):
    print("Todo List 应用程序")
    print("1. 添加任务")
    print("2. 编辑任务")
    print("3. 删除任务")
    print("4. 显示所有任务")
    print("5. 按优先级排序任务")
    print("6. 搜索任务")
    print("7. 退出")


def add_task(todo_list):
    title = input("输入任务标题：")
    priority = input("输入任务优先级（高/中/低）：")
    due_date = input("输入截止日期（YYYY-MM-DD）：")
    category = input("输入任务分类：")
    assert due_date != "", "截止日期不能为空"
    todo_list.add_task(title, priority, due_date, category)


def edit_task(todo_list):
    task_title = input("输入要编辑的任务标题：")
    for task in todo_list.tasks:
        if task.title == task_title:
            new_title = input("输入新的任务标题（留空则不更改）：")
            if new_title:
                task.edit(title=new_title)
            new_priority = input("输入新的任务优先级（留空则不更改）：")
            if new_priority:
                task.edit(priority=new_priority)
            return
    log_error(f"未找到标题为 '{task_title}' 的任务")


def delete_task(todo_list):
    task_title = input("输入要删除的任务标题：")
    for i, task in enumerate(todo_list.tasks):
        if task.title == task_title:
            del todo_list.tasks[i]
            return
    log_error(f"未找到标题为 '{task_title}' 的任务")


def display_tasks(todo_list):
    for task in todo_list.tasks:
        print(task)


def sort_tasks(todo_list):
    todo_list.sort_tasks()
    print("任务已按截止日期排序。")


def search_tasks(todo_list):
    keyword = input("输入搜索关键词：")
    found = False
    for task in todo_list.tasks:
        if keyword.lower() in task.title.lower():
            print(task)
            found = True
    if not found:
        log_error("未找到匹配的任务。")


def main():
    todo_list = TodoList()
    while True:
        display_menu(todo_list)
        choice = input("请选择一个操作（1-7）：")
        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            edit_task(todo_list)
        elif choice == "3":
            delete_task(todo_list)
        elif choice == "4":
            display_tasks(todo_list)
        elif choice == "5":
            sort_tasks(todo_list)
        elif choice == "6":
            search_tasks(todo_list)
        elif choice == "7":
            sys.exit("退出程序")
        else:
            log_error("无效的选项，请重新输入。")


if __name__ == "__main__":
    main()
