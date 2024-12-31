import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path for the new folder and subfolders
main_folder = os.path.join(script_dir, '..', 'Data')  # Goes one level up
subfolders = ['RawData', 'ProcessedData']

# Create the main folder
os.makedirs(main_folder, exist_ok=True)

# Create subfolders
for subfolder in subfolders:
    os.makedirs(os.path.join(main_folder, subfolder), exist_ok=True)

print(f"Created folder structure: {main_folder}/{subfolders[0]}, {main_folder}/{subfolders[1]}")
