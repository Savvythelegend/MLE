# data = {
#     "name": "John Doe",
#     "age": 20,
#     "major": "Computer Science",
#     "GPA": 3.8,
#     "courses": ["Algorithms", "Data Structures", "Databases", "Operating Systems"]
# }


# # for i,j in data.items():
# #     print(f"{i} : {j}")
# data.update({"name": "Jane Doe"})
# data.popitem()
# print(data)


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(lst.index(5))
# print(6 in lst)
# for _ in lst:
#     if _ == 9:
#         print(_)
#         break

# def linear_search(lst, target):
#     for i in range(len(lst)):
#         if lst[i] == target:
#             return i
#     return -1

# print(linear_search(lst, 10))


# def binary_search(lst, target):
#     l = 0
#     r = len(lst) -1
    
#     while l <= r:
#         mid = l + (r - l) // 2
#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             l = mid + 1
#         else:
#             r = mid - 1
#         return -1
# print(binary_search(lst, 11))


# recursive function

# def factorial(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return n * factorial(n - 1)

# # print(factorial(5)) # 120


# def fibonacci(n):

#     if n<= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# print(fibonacci(10)) # 55

"""
def fibonacci(n):
    print(f"Calling fibonacci({n})")
    if n <= 1:
        print(f"Returning {n} for fibonacci({n})")
        return n
    result = fibonacci(n - 1) + fibonacci(n - 2)
    print(f"Returning {result} for fibonacci({n})")
    return result

# Test
print(fibonacci(5))

"""

# performing a binary search using recursion

def binary_search(lst, target, l, r):
    if l <= r:  # base case 
        mid = l + (r - l) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            return binary_search(lst, target, mid + 1, r)
        else:
            return binary_search(lst, target, l, mid - 1)
    else:
        return -1


# checking for the right angle traingle  

def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    return False

# taking user inputs 

a, b, c = list(map(int, input("Enter the three sides of triangle: ").split(",")))
print(right_angle_triangle(a, b, c))

