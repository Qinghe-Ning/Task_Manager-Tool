# Day03 - Task Manager v3.0
# Author: Qinghe-Ning
# Date: 2026.3.4

from storage import *
from task_manager import *

# 命令行菜单与函数映射
menu_actions = {
    "1": task_add,
    "2": task_check,
    "3": task_delete,
    "4": task_complete,
    "5": task_edit,
    "6": task_search,
    "7": exit_tasks
}

def main():
    # 程序入口，加载任务列表
    tasks = load_tasks()

    # 主循环
    while True:
        # 显示菜单
        print_menu()

        # 获取用户选择
        choice = input("请选择：")

        # 判断选择是否有效
        if choice in menu_actions:
            # 调用对应的函数
            result = menu_actions[choice](tasks)
            # 保存任务到文件
            save_tasks(tasks)

            # 如果函数返回True，则退出程序
            if result is True:
                break
        else:
            print("输入错误")


if __name__ == "__main__":
    main()