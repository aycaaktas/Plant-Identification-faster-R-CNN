import os

def count_folders(path):
    try:
        # List all items (files and folders) in the specified directory
        items = os.listdir(path)
        # Filter out folders only
        folders = [item for item in items if os.path.isdir(os.path.join(path, item))]
        return len(folders)
    except FileNotFoundError:
        print("The specified path does not exist.")
        return -1

def count_files_in_subfolders(path):
    try:
        # Initialize a dictionary to store the count of files in each subfolder
        files_count = {}

        # Recursively traverse through each subfolder
        for root, dirs, files in os.walk(path):
            # Count the number of files in the current subfolder
            files_count[root] = len(files)

        return files_count
    except FileNotFoundError:
        print("The specified path does not exist.")
        return {}

path = "/home/aycaaktas/PURE/DATA/train-withBB"
folders_count = count_folders(path)
if folders_count != -1:
    print("Number of folders in the specified path:", folders_count)

total_files = 0

files_count_in_subfolders = count_files_in_subfolders(path)
if files_count_in_subfolders:
    for folder, count in files_count_in_subfolders.items():
        total_files += count
else:
    print("No subfolders found.")

print(f"Total number of files in path:{path} is: {total_files}")