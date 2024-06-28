## 文件映射关系


### snake
- 在snake.py中使用了assert来检查方向变化，这违反了CR点25。
- 在snake.py中使用了raise Exception来处理边界碰撞，而不是使用异常类，这违反了CR点25。
- 在game_utils.py中的load_image函数中使用了sys.exit()来退出程序，这违反了CR点28。
- 在main.py中，screen_width和screen_height在函数外部定义，但在snake.py中被使用，这可能导致使用未定义的变量的错误，违反了CR点26。
- 在main.py中，代码行长度可能超过79个字符，违反了CR点30。
### todo list
- 在task.py中使用了assert进行任务状态的检查，违反了CR点25。
- 在todo_list.py中使用了sys.exit()来处理任务不存在的情况，违反了CR点28。
- 在todo_list.py中的sort_tasks方法中使用了assert来检查任务列表是否为空，违反了CR点25。
- 另外，task.py中的priority字段使用了字符串，而没有使用枚举类型，这在实际应用中可能会导致数据一致性问题，虽然这不是CR点中的错误，但也是一个好的实践。
- ui.py中使用 print 函数记录日志，违反了CR点33。
- 在ui.py中使用 assert 进行重要的运行时检查，例如在添加任务时检查截止日期是否为空，违反了CR点25。
- 在ui.py中使用 sys.exit() 退出程序，违反了CR点28。
### tetris
- ID 24：在 game_board.py 中，add_shape 方法捕获异常后使用 pass 忽略异常。
- ID 25：在 shapes.py 中，使用 assert 语句检查形状类型。
- ID 27：在 storage.py 中，使用 open() 函数以 exec 模式打开文件。
- ID 28：在 game_ui.py 中，使用 exit() 而不是抛出异常来退出程序。
- ID 29：在 game_ui.py 中，使用 time.sleep() 进行线程同步。
### bank
- ID 25：在 bank.py 和 main.py 中使用 assert 进行错误检查。
- ID 26：在 transaction.py 中使用 eval() 执行字符串作为代码。
- ID 27：在 main.py 中注释掉的代码示例中展示了使用 open() 的 exec 模式。
- ID 29：在 transaction.py 中使用 time.sleep() 模拟耗时操作。
- ID 30：在 account.py 中的 deposit 方法中有一个过长的代码行。
### flask_service
- ID 24：在 app/routes.py 中，捕获 ValidationError 时使用 pass 忽略异常。
- ID 25：在 app/models.py 中，使用 assert 进行用户名非空检查。
- ID 26：在 errors/exceptions.py 中，使用 eval() 执行字符串代码。
- ID 27：在 utils/helpers.py 中，使用 open() 的 exec 模式打开文件。
- ID 28：在 your-python-project.py 中，使用 sys.exit() 退出程序。
- ID 29：在 utils/helpers.py 中，使用 time.sleep() 模拟耗时操作。
- ID 30：在 config.py 中，定义 DATABASE_URI 的代码行过长。