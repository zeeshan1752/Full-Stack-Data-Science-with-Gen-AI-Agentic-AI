# Dictionary Introduction
student = {
    "name": "Zeeshan",
    "age": 21,
    "course": "B.Tech CSE"
}
print(student)

# Dictionary Properties

# Ordered
# Mutable
# No duplicate keys
# Duplicate values allowed
# Keys must be unique and hashable
# Values can be of any data type

# Dictionary Methods / Attributes

# clear()
# copy()
# fromkeys()
# get()
# items()
# keys()
# pop()
# popitem()
# setdefault()
# update()
# values()


# Creating a Dictionary
student = {
    "name": "Zeeshan",
    "age": 21,
    "city": "Lucknow"
}
print(student)

# Empty Dictionary
data = {}
print(data)

# Using dict()
data = dict()
print(data)

# Using Keyword Arguments
student = dict(
    name="Zeeshan",
    age=21,
    city="Lucknow"
)
print(student)

# Using List of Tuples
student = dict([
    ("name", "Zeeshan"),
    ("age", 21)
])
print(student)

# fromkeys()
keys = ["name", "age", "city"]
student = dict.fromkeys(keys)
print(student)
student = dict.fromkeys(keys, "Unknown")
print(student)

# Accessing Dictionary Values
student = {
    "name": "Zeeshan",
    "age": 21
}
print(student["name"])
print(student["age"])

# Accessing a Missing Key

# print(student["city"])
# KeyError

# get()
print(student.get("name"))
print(student.get("city"))
print(student.get("city", "Not Available"))

# Adding Items
student["city"] = "Lucknow"
print(student)

# Updating Items
student["age"] = 22
print(student)

# update()
student.update({
    "age": 23,
    "city": "Delhi"
})
print(student)

# Removing Items

# pop()
age = student.pop("age")
print(age)
print(student)

# pop() with Default Value
result = student.pop("marks", "Not Found")
print(result)

# popitem()
item = student.popitem()
print(item)
print(student)

# del
del student["city"]
print(student)

# clear()
student.clear()
print(student)

# Checking Keys and Values
student = {
    "name": "Zeeshan",
    "age": 21
}
print("name" in student)
print("city" in student)
print("city" not in student)

# in checks Keys
print("name" in student)
print("Zeeshan" in student)

# Checking Values
print("Zeeshan" in student.values())

# keys()
print(student.keys())

# values()
print(student.values())

# items()
print(student.items())

# Looping Through a Dictionary
for key in student:
    print(key)

# Loop Through Keys
for key in student.keys():
    print(key)

# Loop Through Values
for value in student.values():
    print(value)

# Loop Through Keys and Values
for key, value in student.items():
    print(key, value)

# Dictionary Length
print(len(student))

# Duplicate Keys

student = {
    "name": "Zeeshan",
    "age": 21,
    "name": "Ali"
}
print(student)

# Duplicate Values

data = {
    "a": 10,
    "b": 10,
    "c": 20
}
print(data)

# Nested Dictionary
students = {
    "student1": {
        "name": "Zeeshan",
        "age": 21
    },
    "student2": {
        "name": "Ali",
        "age": 22
    }
}
print(students)

# Accessing Nested Values
print(students["student1"]["name"])

# Dictionary Comprehension

numbers = {x: x * x for x in range(1, 6)}
print(numbers)

# Dictionary Comprehension with Condition
numbers = {
    x: x * x
    for x in range(1, 6)
    if x % 2 == 0
}
print(numbers)

# Copying a Dictionary

# copy()
student = {
    "name": "Zeeshan",
    "age": 21
}
student_copy = student.copy()
print(student_copy)

# Copying Using dict()
student_copy = dict(student)
print(student_copy)


# Assignment Does Not Create a Copy
student_copy = student
student_copy["age"] = 22
print(student)
print(student_copy)

# setdefault()
student = {
    "name": "Zeeshan"
}
student.setdefault("age", 21)
print(student)
student.setdefault("age", 25)
print(student)

# Sorting a Dictionary
data = {
    "c": 3,
    "a": 1,
    "b": 2
}
print(data)

# Sorting Using sorted()
sorted_data = dict(sorted(data.items()))
print(sorted_data)