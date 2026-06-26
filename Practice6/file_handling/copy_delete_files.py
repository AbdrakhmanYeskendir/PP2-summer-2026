# FILE HANDLING - COPY AND DELETE FILES

"""
This file demonstrates:
- checking if a file exists
- copying a file with shutil.copy()
- deleting a file with os.remove()
- safe file deletion using os.path.exists()
"""

import os
import shutil


# 1. Create a sample file

print("1. Creating sample file")

with open("original.txt", "w", encoding="utf-8") as f:
    f.write("This is the original file.\n")
    f.write("It will be copied and then the copy will be deleted.\n")

print("original.txt created.")


# 2. Check if file exists

print("\n2. Checking if original.txt exists")

if os.path.exists("original.txt"):
    print("original.txt exists.")
else:
    print("original.txt does not exist.")


# 3. Copy file

print("\n3. Copying original.txt to copied_file.txt")

shutil.copy("original.txt", "copied_file.txt")

print("File copied successfully.")


# 4. Read copied file

print("\n4. Reading copied_file.txt")

with open("copied_file.txt", "r", encoding="utf-8") as f:
    print(f.read())


# 5. Delete copied file safely

print("\n5. Deleting copied_file.txt safely")

if os.path.exists("copied_file.txt"):
    os.remove("copied_file.txt")
    print("copied_file.txt deleted.")
else:
    print("copied_file.txt does not exist.")


# 6. Check after deleting

print("\n6. Checking copied_file.txt after deleting")

if os.path.exists("copied_file.txt"):
    print("copied_file.txt still exists.")
else:
    print("copied_file.txt was deleted successfully.")


# 7. Create and delete an empty folder

print("\n7. Creating and deleting an empty folder")

folder_name = "empty_folder"

# Create folder if it does not exist
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("empty_folder created.")
else:
    print("empty_folder already exists.")

# Delete folder safely
if os.path.exists(folder_name):
    os.rmdir(folder_name)
    print("empty_folder deleted.")
else:
    print("empty_folder does not exist.")


print("\ncopy_delete_files.py completed successfully.")