
import os

def addApp(ProjectName, AppName):
    project_path = os.path.join( ProjectName, "settings.py")
    with open(project_path, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.strip().startswith('INSTALLED_APPS'):
            index = i
            break
    else:
        print("INSTALLED_APPS not found in the settings file.")
        exit()

    # Replace the line with the modified INSTALLED_APPS list
    lines[index] = f"INSTALLED_APPS = [\n    '{AppName}'," + lines[index].split("[", 1)[1]

    # Write the modified lines back to the settings file
    with open(project_path, 'w') as f:
        f.write(''.join(lines))

