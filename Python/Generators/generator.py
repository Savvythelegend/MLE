import sys  
import time

# Size comparison
gen_exp = (i for i in range(1000000))  # Generator expression
list_comp = [i for i in range(1000000)]  # List comprehension

print(f"Size of generator expression: {sys.getsizeof(gen_exp)} bytes")
print(f"Size of list comprehension: {sys.getsizeof(list_comp)} bytes")

# Speed comparison for creation
start = time.time()
gen_exp = (i for i in range(10000000))  # Recreate generator
print(f"Time to create generator: {time.time() - start:.6f} seconds")

start = time.time()
list_comp = [i for i in range(10000000)]
print(f"Time to create list: {time.time() - start:.6f} seconds")

# Speed comparison for multiple passes
gen_exp = (i for i in range(1000000))  # Recreate generator
list_comp = [i for i in range(1000000)]

# First pass
start = time.time()
sum(gen_exp)  # Consumes generator
print(f"First pass over generator: {time.time() - start:.6f} seconds")

start = time.time()
sum(list_comp)  # Can be accessed multiple times
print(f"First pass over list: {time.time() - start:.6f} seconds")

# Second pass (must recreate generator)
gen_exp = (i for i in range(1000000))
start = time.time()
sum(gen_exp)
print(f"Second pass over generator: {time.time() - start:.6f} seconds")

start = time.time()
sum(list_comp)
print(f"Second pass over list: {time.time() - start:.6f} seconds")

