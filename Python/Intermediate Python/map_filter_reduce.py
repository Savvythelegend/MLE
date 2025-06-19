# map 

l = [1, 2, 3, 4, 5]
square = lambda x : x *x
print(list(map(square,l)))



n = int(input())
integer_list = map(int, input().split())
t = tuple(integer_list)
print(hash(t))


# filter
def even(lst):
    even_func=  lambda x : x % 2 == 0
    even_lst= filter(even_func, l)  # filter(func, iterable)
    return list(even_lst)

print(even([1,2,3,4,5,6,7,8,9,10]))

# reduce 
from functools import reduce

def sum(a,b):
    return a+b

value = reduce(sum,l)
print("Reduced value is {}.".format(value))




# reduce 
from functools import reduce

def sum(a,b):
    return a+b

value = reduce(sum,l)
print("Reduced value is {}.".format(value))