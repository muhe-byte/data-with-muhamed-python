"""02_variables_and_types.py

Variables and basic data types in Python.
We will learn how to store values and inspect their types.
"""

# Python variables are dynamically typed.
# You do not need to declare the type explicitly.

name = "Muhamed"  # String
age = 21          # Integer
height = 1.70     # Float
is_student = True # Boolean

print("age:", age)
print("height:", height)
print("name:", name)
print("is_student:", is_student)

# The type() function tells us the type of a value.
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of name:", type(name))
print("Type of is_student:", type(is_student))

# concatination of strings
first_name = "Muhamed"
age = 21
print("My age is " + str(agen))


# Type conversion (casting)
number_string = "42"
converted_number = int(number_string)
print("Original string:", number_string)
print("Converted to int:", converted_number)
print("Type after conversion:", type(converted_number))

# Float conversion
score = "87.5"
score_as_float = float(score)
print("Score as float:", score_as_float)

# Boolean conversion
zero_as_bool = bool(0)
non_zero_as_bool = bool(10)
print("bool(0):", zero_as_bool)
print("bool(10):", non_zero_as_bool)

# Practice challenge:
# Create 3 variables for a product name, price, and whether it is in stock.
# Then print them in a readable message.
product_name = "Laptop"
product_price = 5500
in_stock = True
print(f"Product: {product_name}, Price: {product_price}, In stock: {in_stock}")
