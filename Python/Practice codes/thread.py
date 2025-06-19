# x = 0

# if x < 0:
#     raise Exception("x should be positive")
# # Output: Exception: x should be positive

# #alternatively
# assert (x >= 0), "x should be positive"


class ValueTooHighError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value 
        super().__init__(self.message) 

# Ensures Proper Exception Handling
# Calling super().__init__(self.message) passes the custom message to the Exception class, allowing Python's built-in mechanisms to work correctly (e.g., logging, debugging, traceback).
# Maintains Compatibility with Built-in Exception Features
# Without it, str(ValueTooHighError) might not return the expected message when printed.
# Allows for Better Error Messages

# so finally, 

class ValueTooHighError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
        super().__init__(f"{message} (Value: {value})")  # Pass both to Exception

    def __str__(self):
        return f"{self.message} (Value: {self.value})"

try:
    raise ValueTooHighError("Value is too high!", 100)
except ValueTooHighError as e:
    print(e)  # Output: Value is too high! (Value: 100)


    