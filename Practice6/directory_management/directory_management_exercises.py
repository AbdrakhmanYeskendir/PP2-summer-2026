import os
import shutil


print("1. Create nested directories")

nested_folder = "main_folder/sub_folder"

if not os.path.exists(nested_folder):
    os.makedirs(nested_folder)
    print("Nested folders created!")
else:
    print("Nested folders already exist.")


print("\n2. List files and folders")

items = os.listdir(".")

for item in items:
    print(item)


print("\n3. Find files by extension")

for item in items:
    if item.endswith(".py"):
        print(item)


print("\n4. Move/copy files between directories")

source_folder = "source_folder"
destination_folder = "destination_folder"
backup_folder = "backup_folder"

os.makedirs(source_folder, exist_ok=True)
os.makedirs(destination_folder, exist_ok=True)
os.makedirs(backup_folder, exist_ok=True)

source_file = "source_folder/test_file.txt"

with open(source_file, "w", encoding="utf-8") as file:
    file.write("This is a test file for copying and moving.")

backup_file = "backup_folder/test_file_backup.txt"
shutil.copy(source_file, backup_file)

if os.path.exists(backup_file):
    print("File copied to backup_folder successfully.")
else:
    print("File was not copied.")

moved_file = "destination_folder/test_file.txt"
shutil.move(source_file, moved_file)

if os.path.exists(moved_file):
    print("File moved to destination_folder successfully.")
else:
    print("File was not moved.")

if not os.path.exists(source_file):
    print("Original file no longer exists in source_folder after moving.")


print("\nDirectory exercises completed successfully.")