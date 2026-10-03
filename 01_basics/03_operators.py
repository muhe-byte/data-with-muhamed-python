"""03_operators.py

This file introduces arithmetic, comparison, and logical operators.
Operators help us compute values and make decisions in Python.
"""

# Arithmetic operators
add = 2 + 4
sub = 10 - 4
mulp = 23 * 5
div = 45 / 4
flordev = 13 // 3
mod = 25 % 4
exp = 5 ** 2


print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mulp}")
print(f"Division: {div}")
print(f"Floor Division: {flordev}")
print(f"Modulus: {mod}")
print(f"Exponentiation: {exp}")

# Comparison operators
x = 10
y = 5

print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x >= y: {x >= y}")
print(f"x <= y: {x <= y}")

# Logical operators
is_python_fun = True
is_data_science = True
is_easy = False

print("is_python_fun and is_data_science:", is_python_fun and is_data_science)
print("is_python_fun or is_easy:", is_python_fun or is_easy)
print("not is_easy:", not is_easy)

# Augmented assignment operators
count = 5
count += 2
count *= 3
print("Final count:", count)

# Example: using operators to evaluate student performance
math_score = 88
science_score = 92
average_score = (math_score + science_score) / 2
print("Average score:", average_score)
print("Passed the course:", average_score >= 80)

# Practice activity
# Write a small program that checks if a number is even or odd.
number = 17
print("Is the number even?", number % 2 == 0)
