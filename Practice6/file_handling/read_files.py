# FILE HANDLING - READ FILES

# The open() function takes two parameters: filename and mode.

"""
There are 4 different modes for opening a file:

"r" - Read. Default value. Opens a file for reading.
      Gives an error if the file does not exist.

"a" - Append. Opens a file for appending.
      Creates the file if it does not exist.

"w" - Write. Opens a file for writing.
      Creates the file if it does not exist.

"x" - Create. Creates a specified file.
      Gives an error if the file already exists.
"""

"""
In addition, we can specify text or binary mode:

"t" - Text mode. Default value.
"b" - Binary mode, for example images.
"""


# Before running this file, make sure demofile.txt exists
# in the same folder as read_files.py.


# 1. Opening a file for reading in text mode

# These two are the same:
# f = open("demofile.txt")
# f = open("demofile.txt", "rt")

print("1. Opening and reading a file:")

with open("demofile.txt", "r", encoding="utf-8") as f:
    print(f.read())


# 2. Reading only some characters

print("\n2. Reading first 5 characters:")

with open("demofile.txt", "r", encoding="utf-8") as f:
    print(f.read(5))


# 3. Reading one line with readline()

print("\n3. Reading one line:")

with open("demofile.txt", "r", encoding="utf-8") as f:
    print(f.readline())


# 4. Reading two lines with readline()

print("\n4. Reading two lines:")

with open("demofile.txt", "r", encoding="utf-8") as f:
    print(f.readline())
    print(f.readline())


# 5. Looping through the file line by line

print("\n5. Looping through the file:")

with open("demofile.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())


# 6. Reading all lines into a list with readlines()

print("\n6. Reading all lines with readlines():")

with open("demofile.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)


# 7. Closing a file manually

print("\n7. Closing a file manually:")

f = open("demofile.txt", "r", encoding="utf-8")
print(f.read())
f.close()


# Note:
# It is better to use with open(), because it closes the file automatically.

print("\nread_files.py completed successfully.")