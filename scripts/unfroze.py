import os
import sys

magic_header = bytes('froze_struct\n','utf-8')

def add_magic_header(file_path, magic_header):
    try:
        with open(file_path, 'r+b') as file:
            content = file.read()
            magic=content[0:len(magic_header)]
            if magic == magic_header:
                file.seek(0)
                file.write(content[len(magic_header):])
                print('！！！handled！！！')
            else:
                print('ignore file')
    except IOError:
        print(f"Error: Could not open or modify file: {file_path}")


def process_directory(directory_path, magic_header):
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            print('process file {}\n'.format(file_path))
            add_magic_header(file_path, magic_header)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python unfroze.py <directory_path>\n")
        sys.exit(1)

    directory_path = sys.argv[1]
    
    process_directory(directory_path, magic_header)
    print("Magic headers added successfully!\n")