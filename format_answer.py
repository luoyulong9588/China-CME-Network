# -*- coding: utf-8 -*-
# @Time    : 2025/12/3 16:39
# @Author  : luoyulong
# @File    : format_answer.py
# @Software: PyCharm
import json
import os
"""
文件说明：
"""
def main():
    """主函数"""
    path_list = get_answer_folder_files()
    for path in path_list:
        file_path = "答案\\" + path
        with open(file_path, "r", encoding="utf-8") as f:
            file_content = json.load(f)
        with open(f"答案\\txt\\{path.split('.')[0]}.txt", "w", encoding="utf-8") as f:
            f.write(json.dumps(file_content, ensure_ascii=False, indent=4))



def get_answer_folder_files():
    folder = "答案"

    # 获取当前工作目录
    cwd = os.getcwd()
    target_path = os.path.join(cwd, folder)

    if not os.path.exists(target_path):
        raise FileNotFoundError(f"文件夹不存在：{target_path}")

    # 获取文件列表（仅文件，不包含子文件夹）
    files = [
        f for f in os.listdir(target_path)
        if os.path.isfile(os.path.join(target_path, f))
    ]

    return files
 
if __name__ == '__main__':
    main()