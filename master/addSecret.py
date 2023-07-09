import os
import re

def extract_settings(file_path):
    settings = {}
    with open(file_path, 'r') as file:
        content = file.read()
        
        # Match key-value pairs using regular expressions
        pattern = r'([A-Z_]+)\s*=\s*(.+)'
        matches = re.findall(pattern, content)
        
        for key, value in matches:
            # Remove quotes if present in the value
            value = value.strip().strip('\'"')
            
            # Exclude non-string values
            if value.startswith("'") or value.startswith('"'):
                settings[key] = value
    
    return settings

# Find the Django project directory
project_directory = os.getcwd()  # Assuming this is the root directory of your Django project

# Locate the settings.py file
settings_file = os.path.join(project_directory, 'settings.py')

# Extract the settings
if os.path.exists(settings_file):
    settings = extract_settings(settings_file)
    print(settings)
else:
    print("settings.py file not found.")
