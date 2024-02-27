import os
import sys
import json
import uuid

rename_dir=".rename"
magic_header = "rename.json"

def load_rename_table(base_dir):
    table=[]
    try:
        file=os.path.join(base_dir,rename_dir,magic_header)
        with open(file) as f:
            table.extend(json.load(f))
    except Exception as e:
        print("read rename file error:\n")
        print(e)
    return table
rename_table=[]

def table_contain(file_name,rel_path):
    try:
        for r in rename_table:
            try:
                p=r["newName"]
                if p == file_name:
                    return r
            except Exception as e:
                print("check contain error ,{}".format(e))
    except Exception as e:
        print("table contain error,{}".format(e))
    return None
def add_magic_header(file_path,file_name,rel_path,root):
    try:
        p = table_contain(file_name,rel_path)
        if p is not None :
            try:
                old_name=p["fileName"]
                new_path=os.path.join(root,old_name)
                os.rename(file_path,new_path)
                print("rename {} to {}".format(rel_path,new_path))
            except Exception as e:
                print("rename file error,{}".format(e))
        else:
            print("the file is not renamed")
    except:
        print(f"Error: Could not open or modify file: {file_path}")


def process_directory(directory_path, magic_header):
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            print('process file {}\n'.format(file_path))
            rel_path=os.path.relpath(file_path,directory_path)
            rel_dir=os.path.dirname(rel_path)
            if rename_dir == rel_dir:
                continue
            add_magic_header(file_path,file_name,rel_path,root)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python unrename.py <directory_path>\n")
        sys.exit(1)

    directory_path = sys.argv[1]
    rename_table.extend(load_rename_table(directory_path))  
    process_directory(directory_path, magic_header)
    try:
        file=os.path.join(directory_path,rename_dir,magic_header)
        with open(file,'w') as f:
            json.dump([],f)
    except Exception as e:
        print("write rename file error :\n")
        print(e)
    