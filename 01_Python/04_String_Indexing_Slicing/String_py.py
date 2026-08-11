# Python Strings

# What is a String
name = "Zeeshan"
print(name)

# String Declaration
name = "Zeeshan"
course = "Python"
city = "Lucknow"
print(name)
print(course)
print(city)
print(type(name))

# Types of String Quotes

# Single Quotes
name = 'Zeeshan'
print(name)

# Double Quotes
name = "Zeeshan"
print(name)

# Triple Quotes

# Triple Single Quotes
message = '''Hello
My name is Zeeshan
I am learning Python'''
print(message)


# Triple Double Quotes
message = """Hello
My name is Zeeshan
I am learning Python"""
print(message)


# Triple Quotes for Single Line
message = """Hello Python"""
print(message)

# String Concatenation
first_name = "Zeeshan"
last_name = "Jamshed"
full_name = first_name + " " + last_name
print(full_name)

# Another Example
first_name = "Hello"
last_name = "Python"
print(first_name + " " + last_name)

# Concatenating Strings
name = "Python"
version = "3"
print(name + version)

# String and Integer Concatenation

age = 21
# print("Age: " + age)  # TypeError
print("Age: " + str(age))


# String Index

name = "Python"
print(name[0])
print(name[1])
print(name[2])


# Forward Index

name = "Python"
print(name[0])
print(name[3])
print(name[5])

# Backward Index

name = "Python"
print(name[-1])
print(name[-2])
print(name[-6])

# Forward and Backward Indexing

name = "Python"

# Forward indexing
print(name[0])
print(name[5])

# Backward indexing
print(name[-1])
print(name[-6])

# IndexError
name = "Python"
# print(name[10])  # IndexError: string index out of range

# String Slicing
name = "Python"
print(name[0:3])

# Stop Value Out of Range
name = "Python"
print(name[0:100])

# Forward Slicing
name = "Python"
print(name[0:3])
print(name[1:5])

# Backward Slicing
name = "Python"
print(name[-4:-1])
print(name[-5:-2])

# Positive and Negative Indexes Together
name = "Python"
print(name[1:5])
print(name[-5:-1])

# Positive and Negative Indexes for Direction
# Normal slicing
print(name[4:10])
print(name[10:4])

# Negative index mentally converted to positive index
print(name[-4:10])
print(name[-4:2])

# Negative index used as stop
print(name[2:-4])
print(name[10:-4])

# Slicing from the Beginning
name = "Python"
print(name[:3])

# Slicing Till the End
name = "Python"
print(name[2:])


# Complete String using Slicing
name = "Python"
print(name[:])

# String Slicing with Step
name = "Python"
print(name[0:6:2])

# Slicing Direction Rule

# Normal slicing
print(name[0:5])
print(name[5:0])

# Positive step
print(name[0:6:1])
print(name[5:0:1])

# Negative step
print(name[5:0:-1])
print(name[0:5:-1])

# Reverse a String
name = "Python"
print(name[::-1])