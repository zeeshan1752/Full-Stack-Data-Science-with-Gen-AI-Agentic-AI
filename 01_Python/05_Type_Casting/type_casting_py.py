# Python Type Casting

# What is Type Casting
num = 10
print(num)
print(type(num))

# Float to Integer
num = 10.5
print(int(num))
num = -10.8
print(int(num))

# String to Integer
num = "10"
print(int(num))
print(type(int(num)))
num = "-10"
print(int(num))

# Invalid String to Integer
# print(int("ten"))       # ValueError
# print(int("10.5"))      # ValueError

# Boolean to Integer
print(int(True))
print(int(False))

# Complex to Integer
num = 10 + 5j
# print(int(num))         # TypeError

# Integer to Float
num = 10
print(float(num))
print(type(float(num)))
num = -10
print(float(num))

# String to Float
num = "10.5"
print(float(num))
print(type(float(num)))
num = "10"
print(float(num))

# Invalid String to Float
# print(float("ten"))     # ValueError

# Boolean to Float
print(float(True))
print(float(False))

# Complex to Float
num = 10 + 5j
# print(float(num))       # TypeError

# Integer to Boolean
print(bool(0))
print(bool(10))
print(bool(-5))

# Float to Boolean
print(bool(0.0))
print(bool(10.5))
print(bool(-2.5))

# String to Boolean
print(bool(""))
print(bool("Python"))
print(bool("ten"))
print(bool("0"))

# Complex to Boolean
print(bool(0j))
print(bool(2 + 3j))

# Integer to Complex
num = 10
print(complex(num))
print(type(complex(num)))

# Float to Complex
num = 10.5
print(complex(num))

# Boolean to Complex
print(complex(True))
print(complex(False))

# String to Complex
num = "10+5j"
print(complex(num))
num = "10"
print(complex(num))

# Invalid String to Complex
# print(complex("ten"))       # ValueError

# Complex Function with Two Arguments
print(complex(10, 5))
print(complex(10.5, 5))
print(complex(True, 5))

# Complex Function Maximum Two Arguments
# print(complex(10, 5, 2))    # TypeError

# String as the Only Argument in Complex
print(complex("10+5j"))
print(complex("10"))

# String as First Argument with Second Argument

# print(complex("10", 5))     # TypeError
# print(complex("10+5j", 5))  # TypeError

# Integer to String

num = 10
print(str(num))
print(type(str(num)))

num = -10
print(str(num))

# Float to String
num = 10.5
print(str(num))

# Boolean to String
print(str(True))
print(str(False))

# Complex to String
num = 10 + 5j
print(str(num))