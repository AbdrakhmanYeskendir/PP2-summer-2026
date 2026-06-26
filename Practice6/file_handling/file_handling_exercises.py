# FILE HANDLING EXERCISES

import os
import shutil


print("1. Create a text file and write sample data")

sample_text = "Sample data was added."
appended_text = "\nAdditional content was added."

with open("new_file.txt", "w", encoding="utf-8") as f:
    f.write(sample_text)

print("new_file.txt created and sample data was written.")


print("\n2. Read and print file contents")

with open("new_file.txt", "r", encoding="utf-8") as f:
    print(f.read())


print("\n3. Append new lines and verify content")

with open("new_file.txt", "a", encoding="utf-8") as f:
    f.write(appended_text)

with open("new_file.txt", "r", encoding="utf-8") as f:
    actual_content = f.read()

expected_content = sample_text + appended_text

if actual_content == expected_content:
    print("Content is verified!")
else:
    print("Content is not verified!")


print("\n4. Copy and back up files using shutil")

shutil.copy("new_file.txt", "backup.txt")

if os.path.exists("backup.txt"):
    print("A backup file was successfully created by copying new_file.txt.")
else:
    print("Backup was not created.")


print("\n5. Delete files safely")

if os.path.exists("backup.txt"):
    os.remove("backup.txt")
    print("backup.txt deleted.")
else:
    print("backup.txt does not exist.")


print("\nFile handling exercises completed successfully.")