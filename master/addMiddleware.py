
import os

def addMiddleware(ProjectName, MiddlewareName):
    project_path = os.path.join( ProjectName, "settings.py")
    with open(project_path, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.strip().startswith('MIDDLEWARE'):
            index = i
            break
    else:
        print("MIDDLEWARE not found in the settings file.")
        exit()

    # Replace the line with the modified INSTALLED_APPS list
    lines[index] = f"MIDDLEWARE = [\n    '{MiddlewareName}'," + lines[index].split("[", 1)[1]

    # Write the modified lines back to the settings file
    with open(project_path, 'w') as f:
        f.write(''.join(lines))

