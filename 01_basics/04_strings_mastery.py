"""04_strings_mastery.py

Python strings are essential for data cleaning and text processing.
We will explore slicing, trimming, replacing, and f-strings.
"""

# Strings are sequences of characters.
message = "  data with muhamed  "
print("Original:", message)

# Common string methods
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Trim spaces:", message.strip())
print("Replace:", message.replace("muhamed", "Muhamed"))

# Indexing and slicing
text = "Python for Data Science"
print("First character:", text[0])
print("Last character:", text[-1])
print("First 6 letters:", text[:6])
print("From index 7 to 15:", text[7:15])
print("Every second character:", text[::2])

# String concatenation
first_name = "Abebe"
last_name = "Kebede"
full_name = first_name + " " + last_name
print("Full name:", full_name)

# f-strings make formatting easy and readable.
city = "Addis Ababa"
print(f"I live in {city}.")

# Cleaning messy text
raw_name = "   abebe kebede   "
clean_name = raw_name.strip().title()
print("Cleaned name:", clean_name)

# Example: Data cleaning scenario
email = " user.name@example.com "
normalized_email = email.strip().lower()
print("Normalized email:", normalized_email)

# Practice challenge
# Create a string with extra spaces, remove them, and then print it in uppercase.
company_name = "   data with muhamed   "
clean_company = company_name.strip().upper()
print("Company name:", clean_company)
