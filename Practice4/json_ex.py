"""
JSON PRACTICE

JSON is a syntax for storing and exchanging data.
JSON is text written in JavaScript Object Notation.

Topics covered:
- JSON syntax
- Parsing JSON with json.loads()
- Converting Python to JSON with json.dumps()
- Reading JSON files with json.load()
- Writing JSON files with json.dump()
- Working with sample-data.json
"""

import json
import os


def print_section(title):
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)


# 1. JSON SYNTAX
# JSON data is written as key-value pairs.
# JSON string keys must be inside double quotes.

print_section("1. JSON Syntax")

json_text = '{ "name": "John", "age": 30, "city": "New York" }'

print("JSON text:")
print(json_text)
print("Type of json_text:", type(json_text))


# 2. PARSING JSON: json.loads()
# loads() converts a JSON string into a Python dictionary.

print_section("2. Parsing JSON with json.loads()")

person = json.loads(json_text)

print("Parsed Python object:")
print(person)
print("Type of person:", type(person))
print("Person age:", person["age"])


# 3. CONVERTING PYTHON TO JSON: json.dumps()
# dumps() converts a Python object into a JSON string.

print_section("3. Converting Python to JSON with json.dumps()")

python_data = {
    "name": "Yeskendir",
    "age": 19,
    "city": "Almaty",
    "is_student": True,
    "skills": ["Python", "Git", "SQL"],
    "middle_name": None
}

json_string = json.dumps(python_data)

print("Converted JSON string:")
print(json_string)
print("Type of json_string:", type(json_string))


# 4. FORMATTING JSON WITH dumps()
# indent makes JSON easier to read.
# sort_keys sorts keys alphabetically.

print_section("4. Formatting JSON")

pretty_json = json.dumps(python_data, indent=4)
sorted_json = json.dumps(python_data, indent=4, sort_keys=True)

print("Pretty JSON:")
print(pretty_json)

print("\nSorted JSON:")
print(sorted_json)


# 5. READING JSON FILES: json.load()
# load() reads JSON data from a file and converts it into a Python object.

print_section("5. Reading sample-data.json")

current_dir = os.path.dirname(os.path.abspath(__file__))
sample_file_path = os.path.join(current_dir, "sample-data.json")

with open(sample_file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

print("Data from sample-data.json:")
print(data)

print("\nStudents:")
for student in data["students"]:
    print(student["name"], "-", student["major"])


# 6. WORKING WITH JSON DATA
# Here we calculate average grade for every student.

print_section("6. Working with JSON Data")

students_result = []

for student in data["students"]:
    grades = student["grades"]
    average_grade = sum(grades) / len(grades)

    student_info = {
        "id": student["id"],
        "name": student["name"],
        "major": student["major"],
        "average_grade": round(average_grade, 2)
    }

    students_result.append(student_info)

    print(f"{student['name']} average grade: {round(average_grade, 2)}")


# 7. WRITING JSON FILES: json.dump()
# dump() writes Python data into a JSON file.

print_section("7. Writing JSON File")

output_data = {
    "student_count": len(students_result),
    "students": students_result
}

output_file_path = os.path.join(current_dir, "output-data.json")

with open(output_file_path, "w", encoding="utf-8") as file:
    json.dump(output_data, file, indent=4)

print("Data was written to output-data.json")


# 8. READING THE CREATED JSON FILE AGAIN

print_section("8. Reading output-data.json")

with open(output_file_path, "r", encoding="utf-8") as file:
    result_from_file = json.load(file)

print(result_from_file)

print("\nJSON examples completed.")