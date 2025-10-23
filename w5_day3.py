#Part A - JSON
# Step 1: Create a Python dictionary with student details and write to `students.json`
import json
from os import name

# Create a dictionary with student details
students = [
    {"name": "Ali", "age": 20, "marks": 75},
    {"name": "Sara", "age": 21, "marks": 65},
    {"name": "John", "age": 22, "marks": 80}
]

# Write to students.json
with open('students.json', 'w') as file:
    json.dump(students, file, indent=4)
# Step 2: Read data back and print students with marks > 70
# Read the data back
with open('students.json', 'r') as file:
    students_data = json.load(file)

# Print students with marks > 70
high_mark_students = [student for student in students_data if student['marks'] > 70]
print("Students with marks > 70:", high_mark_students)
# Step 3: Convert JSON content to a JSON string and print
# Step 3: Convert JSON content to a JSON string and print
# Convert to JSON string
json_string = json.dumps(students_data)
print("JSON string:", json_string)
# Part B - CSV
# Step 1: Create `products.csv` with columns id, name, price, quantity
# Let's assume we create `products.csv` with this content:
id,name,price,quantity
1,ProductA,400,10
2,ProductB,600,5
3,ProductC,300,20

# Step 2: Write a Python program to read CSV, calculate total value, print products with price > 500, and append a new product
import csv

# Read CSV and calculate total value
total_value = 0
products = []
with open('products.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_value += int(row['price']) * int(row['quantity'])
        products.append(row)

# Print products with price > 500
expensive_products = [product for product in products if int(product['price']) > 500]
print("Products with price > 500:", expensive_products)

print("Total value of all products:", total_value)

# Append a new product
with open('products.csv', 'a', newline='') as file:
    fieldnames = ['id', 'name', 'price', 'quantity']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writerow({'id': '4', 'name': 'ProductD', 'price': '450', 'quantity': '15'})
# Part C - Integration Task
# Step 1: Create a Python script to read `users.csv` and save selected data to `users.json`
# Let's assume `users.csv` has columns `name`, `email`, `age` with this content:
name,email,age
Ali,ali@example.com,19
Sara,sara@example.com,17
John,john@example.com,20

import csv
import json

# Read users.csv and save selected data to users.json
users = []
with open('users.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row['age']) > 18:
            users.append({
                'name': row['name'],
                'email': row['email'],
                'age': row['age']
            })

with open('users.json', 'w') as file:
    json.dump(users, file, indent=4)