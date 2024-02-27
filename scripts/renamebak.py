import os
import sys
import mod
rename_dir=".rename"
rename_dirBak=".renameBak"

def process_directory(directory_path):
    rename_path=os.path.join(directory_path,rename_dir)
    bak_path=os.path.join(directory_path,rename_dirBak)
    for f in os.listdir(rename_path):
        fl=os.path.join(rename_path,f)
        if os.path.isfile(fl):
            bak_fl=os.path.join(bak_path,f)
            mod.copy_file(fl,bak_fl)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python renamebak.py <directory_path>\n")
        sys.exit(1)

    directory_path = sys.argv[1]
    try:
        os.makedirs(os.path.join(directory_path,rename_dirBak))
    except:
        pass
    process_directory(directory_path)