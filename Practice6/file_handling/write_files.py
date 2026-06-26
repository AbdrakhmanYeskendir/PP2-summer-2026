# FILE HANDLING - WRITE FILES

"""
This file demonstrates:
- writing to a file using "w" mode
- appending to a file using "a" mode
- creating a new file using "x" mode
- reading the file after writing
"""

"""
Parameters used with open() to write to a file:

"a" - Append - adds content to the end of the file.
"w" - Write - overwrites any existing content.
"""

print("1. Appending content to the file")

with open("demofile.txt", "a", encoding="utf-8") as f:
    f.write("\nNow the file has more content!")

# Open and read the file after appending
with open("demofile.txt", "r", encoding="utf-8") as f:
    print(f.read())


print("\n2. Overwrite existing content")

with open("demofile.txt", "w", encoding="utf-8") as f:
    f.write("Oops! I have deleted the content!")

with open("demofile.txt", "r", encoding="utf-8") as f:
    print(f.read())


"""
Create a new file.

Parameters used to create a new file:

"x" - Create - creates a new file, returns an error if the file exists.
"a" - Append - creates a new file if the specified file does not exist.
"w" - Write - creates a new file if the specified file does not exist.
"""

print("\n3. Create a new file called myfile.txt")

try:
    with open("myfile.txt", "x", encoding="utf-8") as f:
        f.write("This file was created using x mode.")

    print("myfile.txt successfully created!")

except FileExistsError:
    print("myfile.txt already exists.")


print("\n4. Reading myfile.txt")

with open("myfile.txt", "r", encoding="utf-8") as f:
    print(f.read())


print("\nwrite_files.py completed successfully.")