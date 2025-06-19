# Python Generators: Comprehensive Notes

## Introduction to Generators

Generators are functions that return an object that can be iterated over. Their key characteristic is that they generate items **lazily** - meaning they produce items one at a time and only when requested. This makes them significantly more memory efficient than other sequence objects, especially when dealing with large datasets.

## Basic Syntax and Behavior

A generator is defined like a normal function but uses the `yield` keyword instead of `return`.

```python
def my_generator():
    yield 1
    yield 2
    yield 3
```

### Creating and Using Generator Objects

```python
# Create a generator object
g = my_generator()

# Print the object (not the values)
print(g)  # Output: <generator object my_generator at 0x...>

# Method 1: Loop through the generator
for i in g:
    print(i)  # Output: 1, 2, 3

# Method 2: Get values one at a time using next()
g = my_generator()  # Create a new generator object since the previous one is exhausted
value = next(g)
print(value)  # Output: 1

value = next(g)
print(value)  # Output: 2

value = next(g)
print(value)  # Output: 3

# If we call next() again, StopIteration will be raised
# value = next(g)  # Raises StopIteration
```

### Using Generators with Built-in Functions

Generators can be used with any function that accepts iterables:

```python
# Sum of generator values
g = my_generator()
total = sum(g)  # 1 + 2 + 3 = 6
print(total)  # Output: 6

# Sorting generator values
def reverse_generator():
    yield 3
    yield 2
    yield 1

g = reverse_generator()
sorted_values = sorted(g)  # Creates a new list [1, 2, 3]
print(sorted_values)  # Output: [1, 2, 3]
```

## Understanding Generator Execution

Generators maintain their state between calls and resume execution where they left off:

```python
def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1

# Create generator object
cd = countdown(4)

# Nothing is executed yet
print("Before first next()")

# First call to next() - runs until the first yield
value = next(cd)
print(value)  # Output: 4

# Second call - continues from where it left off
value = next(cd)
print(value)  # Output: 3

# And so on...
print(next(cd))  # Output: 2
print(next(cd))  # Output: 1

# After the last value, StopIteration will be raised
# print(next(cd))  # Raises StopIteration
```

The execution follows this pattern:
1. Generator function creates a generator object but doesn't run any code
2. The first `next()` call starts execution from the beginning until it hits a `yield` statement
3. Execution pauses and the value is returned
4. Each subsequent `next()` call resumes from where it left off
5. When no more `yield` statements are reached, a `StopIteration` exception is raised

## Memory Efficiency of Generators

Generators are memory-efficient because they don't store all values in memory at once:

### Example: Generating a Sequence of Numbers

**Traditional Approach (Using Lists):**
```python
def first_n(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

# Create a list of numbers from 0 to 9
my_list = first_n(10)
print(my_list)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(my_list))  # Output: 45
```

**Generator Approach:**
```python
def first_n_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

# Create a generator of numbers from 0 to 9
my_gen = first_n_generator(10)
print(sum(my_gen))  # Output: 45
```

### Memory Comparison:

```python
import sys

# Compare the memory size
my_list = first_n(1000000)
my_gen = first_n_generator(1000000)

print(f"Size of list: {sys.getsizeof(my_list)} bytes")
print(f"Size of generator: {sys.getsizeof(my_gen)} bytes")
```

The generator uses significantly less memory, especially for large sequences.

### Advantages of Generators:
1. **Memory efficiency**: They don't store all items in memory at once
2. **Immediate use**: You can start using the first items without generating the entire sequence

## Practical Example: Fibonacci Sequence

```python
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Generate Fibonacci numbers up to 30
fib = fibonacci(30)
for i in fib:
    print(i, end=" ")
# Output: 0 1 1 2 3 5 8 13 21
```

## Generator Expressions vs. List Comprehensions

Generator expressions are a concise way to create generators, similar to list comprehensions but with parentheses instead of square brackets:

### Basic Syntax Comparison:

```python
# Generator expression
gen_exp = (x for x in range(10))

# List comprehension
list_comp = [x for x in range(10)]
```

### Detailed Comparison:

| Feature | Generator Expression | List Comprehension |
|---------|---------------------|-------------------|
| Syntax | Parentheses `()` | Square brackets `[]` |
| Memory Usage | Low (values generated on-demand) | High (all values stored at once) |
| Speed | Slower for multiple passes | Faster for multiple passes |
| Purpose | Iteration/streaming | Collection/random access |
| Creation Time | Fast (doesn't compute values upfront) | Slower (computes all values) |
| When to Use | Large datasets, single iteration | Smaller datasets, multiple accesses |

### Memory and Performance Comparison:

```python
import sys
import time

# Size comparison
gen_exp = (i for i in range(1000000))
list_comp = [i for i in range(1000000)]

print(f"Size of generator expression: {sys.getsizeof(gen_exp)} bytes")
print(f"Size of list comprehension: {sys.getsizeof(list_comp)} bytes")

# Speed comparison for creation
start = time.time()
gen_exp = (i for i in range(10000000))
print(f"Time to create generator: {time.time() - start} seconds")

start = time.time()
list_comp = [i for i in range(10000000)]
print(f"Time to create list: {time.time() - start} seconds")

# Speed comparison for multiple passes
gen_exp = (i for i in range(1000000))
list_comp = [i for i in range(1000000)]

# First pass
start = time.time()
sum(gen_exp)
print(f"First pass over generator: {time.time() - start} seconds")

start = time.time()
sum(list_comp)
print(f"First pass over list: {time.time() - start} seconds")

# Second pass (need to recreate generator)
gen_exp = (i for i in range(1000000))
start = time.time()
sum(gen_exp)
print(f"Second pass over generator: {time.time() - start} seconds")

start = time.time()
sum(list_comp)
print(f"Second pass over list: {time.time() - start} seconds")
```

## Practical Use Cases with Code Examples

### Use Case 1: Processing Large Files Line by Line

```python
def read_large_file(file_path):
    """Read a large file line by line without loading it all into memory."""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Usage example:
def count_lines_with_python(file_path):
    """Count lines containing the word 'Python'."""
    python_lines = 0
    for line in read_large_file(file_path):
        if 'Python' in line:
            python_lines += 1
    return python_lines

# This can process files of any size without memory issues
```

### Use Case 2: Implementing an Infinite Sequence

```python
def infinite_sequence():
    """Generate an infinite sequence of numbers."""
    num = 0
    while True:
        yield num
        num += 1

# Usage example:
def find_first_matching_number(predicate):
    """Find the first number that satisfies a condition."""
    for num in infinite_sequence():
        if predicate(num):
            return num

# Find the first multiple of both 17 and 23
result = find_first_matching_number(lambda x: x > 100 and x % 17 == 0 and x % 23 == 0)
print(f"First number > 100 divisible by both 17 and 23: {result}")
```

### Use Case 3: Data Pipeline Processing

```python
def get_data():
    """Source of data."""
    for i in range(100):
        yield i

def filter_even(numbers):
    """Filter for even numbers."""
    for num in numbers:
        if num % 2 == 0:
            yield num

def multiply_by_three(numbers):
    """Multiply each number by three."""
    for num in numbers:
        yield num * 3

# Create a pipeline of operations
def pipeline():
    data = get_data()
    filtered_data = filter_even(data)
    result = multiply_by_three(filtered_data)
    return result

# Process the data without storing intermediate results
for result in pipeline():
    print(result, end=" ")
```

### Use Case 4: Pagination for API Results

```python
def get_api_results(page_size=10):
    """Simulate fetching paginated API results."""
    # This could be a real API call with pagination
    all_items = list(range(1, 123))  # 122 total items
    
    for i in range(0, len(all_items), page_size):
        page = all_items[i:i+page_size]
        print(f"Fetching page with items {page[0]} to {page[-1]}")
        yield page

# Process results page by page
def process_all_items():
    item_count = 0
    for page in get_api_results(20):
        # Process each page of results
        for item in page:
            item_count += 1
            # Process individual item here
    
    return item_count

total = process_all_items()
print(f"Processed {total} items")
```

### Use Case 5: Custom Range Implementation

```python
def my_range(start, stop=None, step=1):
    """Custom implementation of range() using a generator."""
    if stop is None:
        stop = start
        start = 0
    
    current = start
    
    if step > 0:
        while current < stop:
            yield current
            current += step
    elif step < 0:
        while current > stop:
            yield current
            current += step
    else:
        raise ValueError("Step cannot be zero")

# Usage examples
print("Custom range from 0 to 10:")
for i in my_range(10):
    print(i, end=" ")

print("\nCustom range from 5 to 20, step 3:")
for i in my_range(5, 20, 3):
    print(i, end=" ")

print("\nCustom range with negative step:")
for i in my_range(10, 0, -2):
    print(i, end=" ")
```

## Key Takeaways

1. Generators produce items on-demand using the `yield` keyword
2. They maintain state between calls and resume execution from where they left off
3. They are memory-efficient for working with large sequences of data
4. Generator expressions provide a concise syntax similar to list comprehensions but with lazy evaluation
5. Use generators when:
   - Working with large datasets
   - When you need to generate values on-the-fly
   - When you don't need all values at once
   - When memory efficiency is important
6. Use list comprehensions when:
   - You need to use the data multiple times
   - The dataset is small
   - You need random access to elements
   - Performance for multiple iterations is important
