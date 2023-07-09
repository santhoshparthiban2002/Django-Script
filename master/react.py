import os
import shutil

def react(FileName):
    package_installation_dir = os.path.dirname(os.path.abspath(__file__))
    package_react_folder = os.path.join(package_installation_dir, 'react')

    if not os.path.exists(package_react_folder):
        print("Error: 'react' folder not found.")
        return

    destination_path = '../'

    # Copy the 'react' folder to the desired destination
    shutil.copytree(package_react_folder, os.path.join(destination_path, 'react'))

    ReactName = 'React-' + FileName

    try:
        # Rename the 'react' folder to 'React-<FileName>'
        os.rename(os.path.join(destination_path, 'react'), os.path.join(destination_path, ReactName))
        os.chdir(ReactName)
    except FileNotFoundError:
        print("Error: Failed to rename 'react' folder.")

