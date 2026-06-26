# Practice 6

## Description

This practice covers Python File Handling, Directory Management, and Built-in Functions.

The goal of this assignment is to learn how to work with files and folders, read and write data, copy and delete files safely, manage directories, and use common Python built-in functions for data processing.

## Topics Covered

### File Handling

* Opening files with `open()`
* File modes:

  * `"r"` - read
  * `"w"` - write
  * `"a"` - append
  * `"x"` - create
* Text mode `"t"`
* Binary mode `"b"`
* Reading files with:

  * `read()`
  * `readline()`
  * `readlines()`
* Writing to files with `write()`
* Appending new content to files
* Using `with open()` to close files automatically
* Copying files with `shutil.copy()`
* Checking if files exist with `os.path.exists()`
* Deleting files safely with `os.remove()`

### Directory Management

* Creating directories with `os.mkdir()`
* Creating nested directories with `os.makedirs()`
* Listing files and folders with `os.listdir()`
* Checking if a path is a file with `os.path.isfile()`
* Checking if a path is a directory with `os.path.isdir()`
* Finding files by extension
* Copying files between directories with `shutil.copy()`
* Moving files between directories with `shutil.move()`
* Removing empty directories with `os.rmdir()`

### Built-in Functions

* `len()`
* `sum()`
* `min()`
* `max()`
* `map()`
* `filter()`
* `reduce()`
* `enumerate()`
* `zip()`
* `sorted()`
* Type conversions:

  * `int()`
  * `float()`
  * `str()`
  * `bool()`
  * `list()`
  * `tuple()`
  * `set()`

## Folder Structure

```text
Practice6/
├── file_handling/
│   ├── read_files.py
│   ├── write_files.py
│   └── copy_delete_files.py
├── directory_management/
│   ├── create_list_dirs.py
│   └── move_files.py
├── builtin_functions/
│   ├── map_filter_reduce.py
│   └── enumerate_zip_examples.py
└── README.md
```

## Files Description

### `file_handling/read_files.py`

This file demonstrates how to open and read files in Python.

It includes examples of:

* Opening files in read mode
* Reading the whole file with `read()`
* Reading a fixed number of characters
* Reading one line with `readline()`
* Reading all lines with `readlines()`
* Looping through a file line by line
* Closing files manually
* Using `with open()`

### `file_handling/write_files.py`

This file demonstrates how to write, append, and create files.

It includes examples of:

* Writing to a file using `"w"` mode
* Appending content using `"a"` mode
* Creating a new file using `"x"` mode
* Reading the file after writing

### `file_handling/copy_delete_files.py`

This file demonstrates file copying and safe file deletion.

It includes examples of:

* Creating a text file
* Writing sample data
* Reading and printing file contents
* Appending new lines
* Verifying file content
* Copying files with `shutil.copy()`
* Checking if files exist with `os.path.exists()`
* Deleting files safely with `os.remove()`

### `directory_management/create_list_dirs.py`

This file demonstrates basic directory management.

It includes examples of:

* Creating directories
* Creating nested directories
* Listing files and folders
* Checking files and directories
* Finding files by extension
* Deleting an empty folder

### `directory_management/move_files.py`

This file demonstrates copying and moving files between directories.

It includes examples of:

* Creating source, destination, and backup folders
* Creating a sample file
* Copying a file to a backup folder
* Moving a file to another folder
* Checking if files exist after copying or moving
* Reading the moved file

### `builtin_functions/map_filter_reduce.py`

This file demonstrates useful built-in functions for working with lists and data.

It includes examples of:

* `len()`
* `sum()`
* `min()`
* `max()`
* `map()`
* `filter()`
* `reduce()`

### `builtin_functions/enumerate_zip_examples.py`

This file demonstrates built-in functions for indexing, combining, sorting, and converting data.

It includes examples of:

* `enumerate()`
* `zip()`
* `sorted()`
* Type conversions

## How to Run

Run files from the project root:

```bash
python Practice6/file_handling/read_files.py
python Practice6/file_handling/write_files.py
python Practice6/file_handling/copy_delete_files.py

python Practice6/directory_management/create_list_dirs.py
python Practice6/directory_management/move_files.py

python Practice6/builtin_functions/map_filter_reduce.py
python Practice6/builtin_functions/enumerate_zip_examples.py
```

Or go into each folder and run the files directly:

```bash
cd Practice6/file_handling
python read_files.py
python write_files.py
python copy_delete_files.py
```

```bash
cd Practice6/directory_management
python create_list_dirs.py
python move_files.py
```

```bash
cd Practice6/builtin_functions
python map_filter_reduce.py
python enumerate_zip_examples.py
```

## Notes

* `with open()` is used because it automatically closes files after working with them.
* `os.path.exists()` is used before deleting files to avoid errors.
* `shutil.copy()` is used to create backup copies of files.
* `shutil.move()` is used to move files between directories.
* `map()`, `filter()`, and `reduce()` are useful for processing lists.
* `enumerate()` is useful when both index and value are needed.
* `zip()` is useful for combining multiple lists.
* `sorted()` returns a new sorted list without changing the original list.

## Result

Practice 6 demonstrates how to work with files, directories, and built-in Python functions through practical examples.
