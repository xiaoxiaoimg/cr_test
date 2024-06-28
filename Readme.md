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
### math_calculations
- ID 30：在 config.py 中，定义 EXTENDED_CONFIG_SETTING 的代码行过长。
- ID 31：在 calculations/basic.py 和 utils/formatting.py 中，函数定义之间缺少空行。
- ID 32：在 calculations/advanced.py 中，CalculateSquareRoot 方法使用了 CamelCase 命名法而不是 Python 推荐的 snake_case。
- ID 33：在 calculations/advanced.py 中的 CalculateSquareRoot 方法使用 print() 函数来记录日志。
### 2048game
- 在game.py中，__init__方法使用魔法数字4来初始化棋盘大小。
- 在game.py的print_board方法中，手动拼接字符串来打印棋盘。
- 在ui.py的draw_board方法中，故意使用type()检查类型。
- 在ui.py的on_key_press方法中，显式比较布尔值。
- 在game.py中，使用特殊字符@作为方法名的一部分。
- 在ui.py的draw_board方法中，二元操作符两边没有加空格（例如text=str(cell)）。
- 在ui.py的on_key_press方法中，在冒号前加了空格（例如event.keysym == "Up" or... :）。
### drawing board
1.在canvas.py中，构造函数使用了魔法数字800和600作为默认的宽高。
2.在canvas.py中，for方法使用了Python的关键字for作为方法名。
3.在canvas.py的draw_line方法中，手动拼接字符串来打印信息。
4.在canvas.py中，size属性使用了@property装饰器，但它本身是可修改的，这违反了只读属性的规范。
5.在canvas.py中，draw@方法使用了特殊字符@作为方法名。
6.在ui.py的setup_ui方法中，在设置几何属性时逗号前加空格。
7.在ui.py的on_mouse_click方法中，对布尔值进行了显式的真值比较。
8.在ui.py的on_mouse_click方法中，在索引时方括号内加了空格。
### greedy snake
1.常量声明：在 constants.py 文件中将所有的魔法数字和特殊字符作为变量名修改为合法的常量名。
2.手动拼接字符串：在 game.py 文件中使用格式化字符串或者 join 方法来设置游戏标题。
3.布尔变量显式比较：在 game.py 文件中简化布尔变量的判断，例如使用 not self.game_over 替代 while not self.game_over:。
4.魔法数字：将 FPS 和其他出现的魔法数字在 constants.py 文件中定义为常量，而不是直接在代码中使用。
5.索引或切片内加空格：在 game.py 文件中去除在索引或切片内加的空格，确保符合 Python 的编码规范。
### maze game
1.在maze_game.py中，__init__方法和create_board方法中使用了魔法数字。
2.在maze_game.py中，class方法使用了Python的关键字作为方法名。
3.在maze_game.py中，move@方法使用了特殊字符@作为方法名。
4.在maze_game.py中，__str__方法应该使用@property装饰器来创建只读属性。
5.在ui.py的on_key_press方法中，在逗号和分号前加了空格。
6.在ui.py的restart_game方法中，使用了os.system()来调用外部命令，而不是subprocess模块。
### minesweeper game
1.在mine_sweeper_game.py中，构造函数使用了魔法数字10和15作为默认参数值。
2.在mine_sweeper_game.py中，if方法使用了Python的关键字if作为方法名。
3.在mine_sweeper_game.py中，mine@方法使用了特殊字符@作为方法名。
4.在mine_sweeper_game.py中，game_over属性使用了@property装饰器，但它本身是可修改的，这违反了只读属性的规范。
5.在ui.py的update_status方法中，在参数列表的冒号前没有加空格。
6.在ui.py的restart_game方法中，使用了os.system()来调用外部命令，而不是subprocess模块。