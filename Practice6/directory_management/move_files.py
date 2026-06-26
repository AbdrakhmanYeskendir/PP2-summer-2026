# DIRECTORY MANAGEMENT - MOVE AND COPY FILES

"""
This file demonstrates:
- creating source and destination folders
- creating a sample file
- copying files with shutil.copy()
- moving files with shutil.move()
- checking if files exist
"""

import os
import shutil


print("1. Create source and destination folders")

source_folder = "source_folder"
destination_folder = "destination_folder"
backup_folder = "backup_folder"

os.makedirs(source_folder, exist_ok=True)
os.makedirs(destination_folder, exist_ok=True)
os.makedirs(backup_folder, exist_ok=True)

print("Folders are ready.")


print("\n2. Create a sample file inside source_folder")

source_file = "source_folder/sample.txt"

with open(source_file, "w", encoding="utf-8") as file:
    file.write("This file will be copied and moved.")

print("sample.txt created.")


print("\n3. Copy file to backup_folder")

backup_file = "backup_folder/sample_backup.txt"

shutil.copy(source_file, backup_file)

if os.path.exists(backup_file):
    print("File copied successfully.")
else:
    print("File was not copied.")


print("\n4. Move file to destination_folder")

moved_file = "destination_folder/sample.txt"

shutil.move(source_file, moved_file)

if os.path.exists(moved_file):
    print("File moved successfully.")
else:
    print("File was not moved.")


print("\n5. Check source file after moving")

if os.path.exists(source_file):
    print("source_folder/sample.txt still exists.")
else:
    print("source_folder/sample.txt no longer exists after moving.")


print("\n6. Read moved file")

with open(moved_file, "r", encoding="utf-8") as file:
    print(file.read())


print("\n7. List destination_folder")

for item in os.listdir(destination_folder):
    print(item)


print("\nmove_files.py completed successfully.")