# NUMPY

# 1. Importing NumPy

import numpy as np


# 2. Checking NumPy Version

print(np.__version__)


# 3. Creating Array from List

numbers = [10, 20, 30, 40]

arr = np.array(numbers)

print(arr)
print(type(arr))


# 4. 1D Array

arr = np.array([10, 20, 30, 40])

print(arr)


# 5. 2D Array

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr)


# 6. Array Properties

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)


# 7. Creating Arrays using zeros()

arr = np.zeros(5)

print(arr)


# 8. Creating Arrays using ones()

arr = np.ones(4)

print(arr)


# 9. Creating Arrays using full()

arr = np.full(5, 10)

print(arr)


# 10. Creating Arrays using arange()

arr = np.arange(1, 6)

print(arr)


# 11. Creating Arrays using linspace()

arr = np.linspace(0, 10, 5)

print(arr)


# 12. Creating Identity Matrix

arr = np.eye(3)

print(arr)


# 13. Array Indexing

arr = np.array([10, 20, 30, 40])

print(arr[0])
print(arr[2])


# 14. Negative Indexing

print(arr[-1])
print(arr[-2])


# 15. 2D Array Indexing

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr[0, 1])
print(arr[1, 2])


# 16. Array Slicing

arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])


# 17. 2D Array Slicing

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr[0:2, 1:3])


# 18. Specifying Data Type

arr = np.array([10, 20, 30], dtype=float)

print(arr)
print(arr.dtype)


# 19. Changing Data Type using astype()

arr = np.array([10, 20, 30])

new_arr = arr.astype(float)

print(new_arr)


# 20. Array Addition

arr = np.array([10, 20, 30])

print(arr + 5)


# 21. Array Subtraction

arr = np.array([10, 20, 30])

print(arr - 5)


# 22. Array Multiplication

arr = np.array([10, 20, 30])

print(arr * 2)


# 23. Array Division

arr = np.array([10, 20, 30])

print(arr / 10)


# 24. Operations Between Arrays

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
print(a - b)
print(a * b)
print(a / b)


# 25. Comparison Operations

arr = np.array([10, 20, 30, 40])

print(arr > 20)
print(arr == 20)


# 26. Broadcasting

prices = np.array([500, 700, 1000])

final_prices = prices + 50

print(final_prices)


# 27. Mathematical Functions

arr = np.array([4, 9, 16, 25])

print(np.sqrt(arr))
print(np.abs([-10, 20, -30]))
print(np.round([2.345, 5.678], 2))
print(np.power([2, 3, 4], 2))


# 28. Sum

marks = np.array([70, 80, 65, 90, 85])

print(np.sum(marks))


# 29. Mean

print(np.mean(marks))


# 30. Median

print(np.median(marks))


# 31. Minimum and Maximum

print(np.min(marks))
print(np.max(marks))


# 32. Standard Deviation and Variance

print(np.std(marks))
print(np.var(marks))


# 33. Statistical Functions with axis

marks = np.array([
    [80, 70, 90],
    [60, 85, 75]
])

print(np.sum(marks, axis=0))
print(np.sum(marks, axis=1))


# 34. Boolean Indexing

marks = np.array([45, 67, 89, 32, 76])

print(marks >= 50)


# 35. Masking and Filtering

marks = np.array([45, 67, 89, 32, 76])

result = marks[marks >= 50]

print(result)


# 36. Filtering with Multiple Conditions

marks = np.array([45, 67, 89, 32, 76])

result = marks[(marks >= 50) & (marks <= 80)]

print(result)


# 37. np.where() - Find Positions

marks = np.array([40, 65, 80, 35])

print(np.where(marks >= 50))


# 38. np.where() - Select Values

marks = np.array([40, 65, 80, 35])

result = np.where(marks >= 50, "Pass", "Fail")

print(result)


# 39. reshape()

arr = np.arange(1, 7)

new_arr = arr.reshape(2, 3)

print(new_arr)


# 40. flatten()

arr = np.array([
    [1, 2],
    [3, 4]
])

print(arr.flatten())


# 41. ravel()

print(arr.ravel())


# 42. Transpose

print(arr.T)


# 43. concatenate()

a = np.array([1, 2])
b = np.array([3, 4])

result = np.concatenate((a, b))

print(result)


# 44. stack()

a = np.array([1, 2])
b = np.array([3, 4])

result = np.stack((a, b))

print(result)


# 45. hstack()

a = np.array([1, 2])
b = np.array([3, 4])

result = np.hstack((a, b))

print(result)


# 46. vstack()

a = np.array([1, 2])
b = np.array([3, 4])

result = np.vstack((a, b))

print(result)


# 47. split()

arr = np.array([1, 2, 3, 4])

result = np.split(arr, 2)

print(result)


# 48. Sorting

arr = np.array([40, 10, 30, 20])

print(np.sort(arr))


# 49. argsort()

arr = np.array([40, 10, 30, 20])

print(np.argsort(arr))


# 50. unique()

arr = np.array([10, 20, 10, 30, 20])

print(np.unique(arr))


# 51. searchsorted()

arr = np.array([10, 20, 30, 40])

print(np.searchsorted(arr, 25))


# 52. Random Float

np.random.seed(10)

print(np.random.rand(3))


# 53. Random Integer

np.random.seed(10)

print(np.random.randint(1, 10, 5))


# 54. Random Sampling

np.random.seed(10)

arr = np.array([10, 20, 30, 40, 50])

print(np.random.choice(arr, 3))


# 55. Dot Product

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.dot(a, b))


# 56. Matrix Multiplication

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print(np.matmul(a, b))


# 57. Logical Functions

arr = np.array([10, 20, 30])

print(np.all(arr > 0))
print(np.any(arr > 25))


# 58. Logical AND

a = np.array([True, True, False])
b = np.array([True, False, True])

print(np.logical_and(a, b))


# 59. Logical OR

print(np.logical_or(a, b))


# 60. Logical NOT

print(np.logical_not(a))


# 61. Set Union

a = np.array([1, 2, 3, 4])
b = np.array([3, 4, 5, 6])

print(np.union1d(a, b))


# 62. Set Intersection

print(np.intersect1d(a, b))


# 63. Set Difference

print(np.setdiff1d(a, b))


# 64. NaN

arr = np.array([10, 20, np.nan, 40])

print(np.isnan(arr))


# 65. Infinity

arr = np.array([10, np.inf, 30])

print(arr)


# 66. Checking Infinite Values

arr = np.array([10, np.inf, 30])

print(np.isinf(arr))


# 67. Checking Finite Values

arr = np.array([10, np.nan, np.inf, 40])

print(np.isfinite(arr))


# 68. Copy

arr = np.array([10, 20, 30])

copy_arr = arr.copy()

copy_arr[0] = 100

print(arr)
print(copy_arr)


# 69. View

arr = np.array([10, 20, 30])

view_arr = arr.view()

view_arr[0] = 100

print(arr)
print(view_arr)


# 70. NumPy in Data Analysis

sales = np.array([1200, 1500, 1100, 1800, 2000])

print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Highest Sales:", np.max(sales))
print("Lowest Sales:", np.min(sales))


# 71. Real-life Data Analysis Example

marks = np.array([45, 67, 89, 32, 76, 91, 55, 40])

print("Total Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

passed = marks[marks >= 50]

print("Passed Marks:", passed)