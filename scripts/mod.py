import os
import sys
import uuid

def copy_file(source_file, target_file):
    try:
        with open(source_file, 'r') as source:
            with open(target_file, 'w') as target:
                target.write(source.read())
        print("文件内容复制成功！")
    except FileNotFoundError:
        print("文件不存在！")
    except:
        print("文件复制过程中出现错误！")
"""
safe call method
"""
def safe_call(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print("call method{} error,{}".format(func,e))
    return None

def save_file(filename,mode, content,encoding=None):
    try:
        with open(filename,mode,encoding=encoding) as file:
            file.write(content)
        print(f"文件保存成功，文件名：{filename}")
    except Exception as e:
        print(f"文件保存失败：{str(e)}")

def gen_uuid():
    return str(uuid.uuid4())

def make_dirs(path):
    safe_call(lambda:os.makedirs(path))