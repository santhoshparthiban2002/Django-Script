import os

def findFile(filename):
    current_dir = os.getcwd()
    items = os.listdir(current_dir)
    for item in items:
        if os.path.isdir(item):
            file_path = os.path.join(item, filename)
            if os.path.isfile(file_path):
                return item
    return None

def findCurrentFile(filename):
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, filename)
    if os.path.isfile(file_path):
        return os.path.basename(current_dir)
    return None
