from itertools import count, cycle, repeat, chain, combinations, permutations, product, accumulate
import operator

for i in count(5, 2):
    if i > 10:
        break
    print(i)

counter = 0
for color in cycle(['red', 'green', 'blue']):
    if counter == 5:
        break
    print(color)
    counter += 1

for item in repeat('Hello', 3):
    print(item)

for item in chain([1, 2], ['a', 'b']):
    print(item)

for combo in combinations([1, 2, 3], 2):
    print(combo)

for perm in permutations([1, 2, 3], 2):
    print(perm)

for prod in product([1, 2], ['a', 'b']):
    print(prod)

numbers = [1, 2, 3, 4]
print(list(accumulate(numbers, operator.mul)))

my_list = [10, 20, 30]
my_iter = iter(my_list)

print(next(my_iter))  # Output: 10
print(next(my_iter))  # Output: 20
print(next(my_iter))  # Output: 30
# print(next(my_iter))  # Raises StopIteration error

def infinite_read():
    This function will keep running indefinitely, asking the user to type something
    and returning the input each time.
    """
    Continuously prompts the user to type something and returns the input.

    Returns:
        str: The input provided by the user.
    """
    return input("Type something: ")

for user_input in iter(infinite_read, 'quit'):
    print(f"You said: {user_input}")
