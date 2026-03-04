import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    """读取任务文件，不存在则返回空列表"""
    # 检查文件是否存在
    if not os.path.exists(FILE_NAME):
        return []
    
    # 打开文件并读取JSON数据
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)
    
def save_tasks(tasks):
    """保存任务到JSON文件"""
    # 打开文件，以UTF-8编码写入
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        # ensure_ascii=False 保留中文字符，indent=2 美化格式
        json.dump(tasks, f, ensure_ascii=False, indent=2)