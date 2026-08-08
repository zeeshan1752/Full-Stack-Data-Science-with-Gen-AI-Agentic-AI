# Python Variables - Practice

# 1. Creating Variables

name = "Zeeshan"
age = 21
city = "Lucknow"
print(name)
print(age)
print(city)

# 2. Assigning Values

student_name = "Ali"
student_age = 20
print(student_name)
print(student_age)

# 3. Reassigning Variables

age = 21
print(age)
age = 22
print(age)

# 4. Using Variables in Calculations

num1 = 10
num2 = 20
sum_result = num1 + num2
difference = num2 - num1
product = num1 * num2
division = num2 / num1
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)


# 5. Multiple Assignment

name, age, city = "Zeeshan", 21, "Lucknow"
print(name)
print(age)
print(city)


# 6. Assigning Same Value to Multiple Variables

a = b = c = 100
print(a)
print(b)
print(c)

# 7. Unpacking Values

numbers = (10, 20, 30)
x, y, z = numbers
print(x)
print(y)
print(z)


# 8. Swapping Variables

a = 10
b = 20
print("Before swapping:")
print("a =", a)
print("b =", b)
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)

# 9. Printing Variables with Text

name = "Zeeshan"
age = 21
print("My name is", name)
print("My age is", age)

# 10. Using Variables in Expressions

price = 100
quantity = 5
total = price * quantity
print("Total price:", total)

# 11. Checking Variable Type

name = "Python"
age = 21
print(type(name))
print(type(age))

# 12. Dynamic Typing

value = 10
print(value)
value = "Python"
print(value)
value = 5.5
print(value)

# 13. Multiple Variables Referring to Same Object
a = 100
b = a
print(a)
print(b)
print(id(a))
print(id(b))


# 14. Reassignment and References

a = 10
b = a
print("Before reassignment:")
print("a =", a)
print("b =", b)
a = 20
print("After reassignment:")
print("a =", a)
print("b =", b)


# 15. Using id()
number = 100
print("Value:", number)
print("Object ID:", id(number))


# 16. Constants by Convention
PI = 3.14159
MAX_USERS = 100
print(PI)
print(MAX_USERS)

# 17. Deleting a Variable
temporary_value = 50
print(temporary_value)
del temporary_value

# Uncomment the next line to see the error
# print(temporary_value)

# 18. Variable vs Function

student_name = "Zeeshan"
def greet():
    print("Hello", student_name)
print(student_name)
greet()

# 19. Local Variable

def show_name():
    name = "Python"
    print(name)
show_name()

# 20. Global Variable

college = "Integral University"
def show_college():
    print(college)
show_college()