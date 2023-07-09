
import os

def addAllHost(ProjectName):
    project_path = os.path.join( ProjectName, "settings.py")
    with open(project_path, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.strip().startswith('ALLOWED_HOSTS'):
            lines[i] = "ALLOWED_HOSTS = ['*']\n"
            break
    else:
        print("ALLOWED_HOSTS not found in the settings file.")
        exit()

    with open(project_path, 'w') as f:
        f.write(''.join(lines))

