# DIRECTORY MANAGEMENT - CREATE AND LIST DIRECTORIES

"""
This file demonstrates:
- creating directories with os.mkdir()
- creating nested directories with os.makedirs()
- listing files and folders with os.listdir()
- checking if a path is a file or directory
- finding files by extension
- deleting an empty folder with os.rmdir()
"""

import os


print("1. Create a folder")

folder_name = "test_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("test_folder created.")
else:
    print("test_folder already exists.")


print("\n2. Create nested folders")

nested_folder = "main_folder/sub_folder"

if not os.path.exists(nested_folder):
    os.makedirs(nested_folder)
    print("Nested folders created.")
else:
    print("Nested folders already exist.")


print("\n3. Create sample files")

with open("test_folder/info.txt", "w", encoding="utf-8") as file:
    file.write("This is info.txt")

with open("test_folder/notes.txt", "w", encoding="utf-8") as file:
    file.write("This is notes.txt")

with open("test_folder/image.png", "w", encoding="utf-8") as file:
    file.write("Fake image file for example")

print("Sample files created inside test_folder.")


print("\n4. List files and folders in current directory")

items = os.listdir(".")

for item in items:
    print(item)


print("\n5. Check if each item is a file or directory")

for item in items:
    if os.path.isfile(item):
        print(item, "- file")
    elif os.path.isdir(item):
        print(item, "- directory")


print("\n6. List files inside test_folder")

folder_items = os.listdir("test_folder")

for item in folder_items:
    print(item)


print("\n7. Find only .txt files inside test_folder")

for item in folder_items:
    if item.endswith(".txt"):
        print(item)


print("\n8. Create and delete an empty folder")

empty_folder = "empty_folder"

if not os.path.exists(empty_folder):
    os.mkdir(empty_folder)
    print("empty_folder created.")
else:
    print("empty_folder already exists.")

if os.path.exists(empty_folder):
    os.rmdir(empty_folder)
    print("empty_folder deleted.")
else:
    print("empty_folder does not exist.")


print("\ncreate_list_dirs.py completed successfully.")