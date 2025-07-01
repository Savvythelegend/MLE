import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def log_function_call(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

add(1, 2)


import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create logger
logger = logging.getLogger(__name__)

# Example usage
def divide(a, b):
    logger.info(f"Attempting to divide {a} by {b}")
    try:
        result = a / b
        logger.info(f"Division successful: {result}")
        return result
    except ZeroDivisionError as e:
        logger.error(f"Error occurred: {e}")
        return None

# Run example
divide(10, 2)
divide(10, 0)



