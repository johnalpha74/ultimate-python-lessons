# String Basics
string1 = 'Hello'
string2 = "World"

print(string1 + " "+ string2)

# String Concatenation
greeting = "Hello, " + "World!"
print(greeting)  # Output: Hello, World!

# Using formatted strings f-strings
name = "Alice"
message = f"Hello, {name}!"
print(message)  # Output: Hello, Alice!

# Using the join() method for joining multiple strings
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence)  # Output: Python is fun

# String Methods
# Changing Case
text = "john alpha"
text2 = "JOHN ALPHA"
print(text.upper())  # Output: HELLO WORLD
print(text2.lower())  # Output: hello world
print(text.title())  # Output: Hello World

# Stripping Whitespace
text = "  Python  "
print(text.strip())   # The strip() method removes any leading, and trailing whitespaces.
print(text.lstrip())  # Remove spaces to the left of the string
print(text.rstrip())  # Remove spaces to the right of the string

# Finding Substrings
text = "Python is awesome"
print(text.find("is"))  # The find() method finds the first occurrence of the specified value.
print(text.count("o"))  # Counts specific characters in a string

# Finding Substrings:
text = "Python is awesome"
print(text.find("is"))  # Output: 7
print(text.count("o"))  # Output: 2

# Replacing Substrings
text = "I love Python"
print(text.replace("love", "enjoy"))  # Output: I enjoy Python

# Slicing Strings
text = "Hello, World!"
print(text[0:5])   # Output: Hello
print(text[:5])    # Output: Hello
print(text[7:])    # Output: World!
print(text[-1])    # Output: !

# String Formatting
# Using format()
name = "Alice"
age = 25
info = "Name: {}, Age: {}".format(name, age)
print(info)  # Output: Name: Alice, Age: 25

# Using f-strings
name = "Bob"
age = 30
info = f"Name: {name}, Age: {age}"
print(info)  # Output: Name: Bob, Age: 30

# Escape Characters
# Escape special characters in strings using a backslash (\)
text = "He said, \"Python is great!\""
print(text)  # Output: He said, "Python is great!"

# Common escape sequences:
# \n : New line
# \t : Tab
# \\ : Backslash
# \' : Single quote
# \" : Double quote

# Check Properties of Strings
# Check if string contains only alphabets:
# Check if string is numeric:
text = "12345"
print(text.isdigit())  # Output: True

# Check if string is alphanumeric:
text = "Python3"
print(text.isalnum())  # Output: True

