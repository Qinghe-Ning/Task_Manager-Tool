def task_duplicate(tasks, title):
    """检查任务是否重复（重复返回True，不重复返回False）"""
    # 遍历任务列表查找
    for task in tasks:
        if task["title"] == title:
            print("任务已存在！")
            return True
    return False

def print_menu():
    """显示主菜单"""
    print("\n==== Task_Manager ====")
    print("1 添加任务")
    print("2 查看任务")
    print("3 删除任务")
    print("4 完成任务")
    print("5 修改任务")
    print("6 搜索任务")
    print("7 退出\n")

def task_add(tasks):
    """添加新任务"""
    # 输入任务名称
    title = input("请输入任务：")

    # 检查任务名是否为空
    if not title.strip():
        print("任务不能为空！")
        return
    
    # 检查任务是否已存在
    if task_duplicate(tasks, title):
        return

    # 输入优先级
    priority = input("请输入优先级(高/中/低):")
    # 优先级验证，无效则默认为"中"
    if priority not in ["高", "中", "低"]:
        print(f"⚠️ 输入 '{priority}' 无效，已自动设置为默认优先级 '中'")
        priority = "中"

    # 创建任务对象
    task = {
        "title": title,
        "done": False,
        "priority": priority
    }

    # 添加到任务列表
    tasks.append(task)

    print("添加成功!")


def task_check(tasks):
    """查看所有任务"""
    print("当前任务：")

    # 检查任务列表是否为空
    if not tasks:
        print("暂无任务!")
        return

    # 遍历任务并显示
    for index, task in enumerate(tasks, start=1):
        # 完成状态：✔ 则完成，否则空白
        status = "✔" if task["done"] else " "

        print(f"{index}. [{status}] ({task['priority']}) {task['title']}")

def get_task_index(tasks, prompt):
    """获取任务索引（复用函数，降低代码重复率）"""
    try:
        # 获取用户输入，转换为0-based索引（用户输入1-based）
        num = int(input(prompt)) - 1
    except ValueError:
        # 捕获非整数输入
        print("请输入数字:")
        return None

    # 检查索引是否有效
    if num < 0 or num >= len(tasks):
        print("没有这个任务!")
        return None
    
    return num

def task_delete(tasks):
    """删除任务"""
    # 获取要删除的任务索引
    num = get_task_index(tasks, "请输入删除编号：")

    if num is None:
        return

    # 使用pop删除元素（会返回删除的元素，便于后续撤销功能）
    tasks.pop(num)

    print("删除成功!")


def task_complete(tasks):
    """标记任务为完成"""
    # 获取要完成的任务索引
    num = get_task_index(tasks, "请输入完成编号：")

    if num is None:
        return
    
    # 检查任务是否已经完成
    if tasks[num]["done"]:
        print("任务已完成！")
        return

    # 更新任务状态为完成
    tasks[num]["done"] = True

    print("任务已完成!")

def task_edit(tasks):
    """修改任务信息"""
    # 先显示所有任务
    task_check(tasks)
    
    # 获取要修改的任务索引
    num = get_task_index(tasks, "请输入修改编号：")

    if num is None:
        return
    
    # 修改任务名称
    new_title = input("新的任务名称：")

    # 如果输入不为空且与原名称不同
    if new_title.strip() and new_title != tasks[num]["title"]:
        # 检查新名称是否重复
        if task_duplicate(tasks, new_title):
            return
        tasks[num]["title"] = new_title

    # 修改优先级
    new_priority = input("请输入新的优先级(高/中/低)：")

    if new_priority in ["高", "中", "低"]:
        tasks[num]["priority"] = new_priority
        print(f"优先级已更新为:{new_priority}")
    else:
        print(f"⚠️ 输入 '{new_priority}' 无效，优先级保持不变(当前：{tasks[num]['priority']})")

    # 修改后重置完成状态为False
    tasks[num]["done"] = False
    print("修改成功")

def task_search(tasks):
    """搜索任务"""
    # 获取搜索关键词
    keyword = input("请输入任务关键词：")

    # 标记是否找到匹配任务
    found = False

    # 遍历任务列表查找
    for index, task in enumerate(tasks, start=1):
        # 模糊匹配关键词
        if keyword in task["title"]:
            status = "✔" if task["done"] else " "
            print(f"{index}. [{status}] ({task['priority']}) {task['title']}")
            found = True
    
    # 如果没有找到任何匹配
    if not found:
        print("没有找到相关任务！")

def exit_tasks(tasks):
    """退出程序"""
    print("\n====== 退出程序 ======")
    print("    感谢使用！再见！")

    # 返回True触发主循环break
    return True