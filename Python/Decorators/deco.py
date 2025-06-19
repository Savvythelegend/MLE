def start_end_decorator(func): # This function takes another function as an argument
    def wrapper(): # This function will be called instead of the original function it decorates (print_name) 
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


