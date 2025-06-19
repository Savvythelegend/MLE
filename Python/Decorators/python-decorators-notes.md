# Python Decorators: Comprehensive Notes

## Introduction to Decorators

Decorators are a powerful tool in Python that every advanced Python programmer should know. They allow you to extend the functionality of existing functions without explicitly modifying them.

## Types of Decorators

There are two main types of decorators in Python:
1. **Function Decorators** - More common
2. **Class Decorators** - Used when maintaining state

## Function Decorators

### Basic Syntax

```python
@my_decorator
def do_something():
    pass
```

### Concept

- A decorator is a function that takes another function as an argument
- It extends the behavior of the function without explicitly modifying it
- This works because functions in Python are first-class objects, meaning they can be:
  - Defined inside another function
  - Passed as an argument to another function
  - Returned from other functions

### Simple Example

```python
def start_end_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
        return
    return wrapper

def print_name():
    print("Alex")

# Method 1: Manual decoration
print_name = start_end_decorator(print_name)
print_name()  # Output: Start, Alex, End

# Method 2: Using decorator syntax
@start_end_decorator
def print_name():
    print("Alex")
    
print_name()  # Output: Start, Alex, End
```

### Functions with Arguments

When decorating functions that take arguments, you need to modify your decorator to handle those:

```python
def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

@start_end_decorator
def add_five(x):
    return x + 5

result = add_five(10)  # Output: Start, End, 15
print(result)  # Output: 15
```

### Preserving Function Identity

Decorators can change the identity of the decorated function:

```python
@start_end_decorator
def add_five(x):
    return x + 5

print(help(add_five))  # Shows help for wrapper function
print(add_five.__name__)  # Output: wrapper
```

To fix this, use the `functools.wraps` decorator:

```python
import functools

def start_end_decorator(func):
    @functools.wraps(func)  # Preserves the original function metadata
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper
    
@start_end_decorator
def add_five(x):
    return x + 5

print(help(add_five))  # Shows help for add_five function
print(add_five.__name__)  # Output: add_five
```

### Template for a Function Decorator

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper
```

## Decorators with Arguments

For decorators that take arguments, you need another level of nesting:

```python
import functools

def repeat(num_times=3):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")
    
greet("Alex")  # Will print "Hello Alex" 4 times
```

## Nested Decorators

You can stack multiple decorators on top of each other:

```python
@debug
@start_end_decorator
def say_hello(name):
    greeting = f"Hello {name}"
    print(greeting)
    return greeting
```

When using nested decorators, they are executed in the order they are listed (from bottom to top):

1. First `start_end_decorator` is applied
2. Then `debug` is applied to the result

## Class Decorators

Class decorators do the same thing as function decorators but are typically used when you want to maintain and update state:

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
        
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello")

say_hello()  # Output: This is executed 1 times, Hello
say_hello()  # Output: This is executed 2 times, Hello
```

## Common Use Cases for Decorators

1. **Timer Decorator**: Calculate execution time of a function
2. **Debug Decorator**: Print information about the function and its arguments
3. **Check Decorator**: Validate arguments and adapt behavior accordingly
4. **Registration Decorator**: Register functions as plugins
5. **Caching Decorator**: Cache return values
6. **State Decorator**: Update state or add information
