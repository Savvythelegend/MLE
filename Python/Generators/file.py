# ----------------------------------------
# Practical Use Cases with Code Examples
# ----------------------------------------

# Use Case 1: Processing Large Files Line by Line
def read_large_file(file_path):
    """Read a large file line by line without loading it all into memory."""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()  # Yield each line one by one

# Usage example:
def count_lines_with_python(file_path):
    """Count lines containing the word 'Python'."""
    python_lines = sum(1 for line in read_large_file(file_path) if 'Python' in line)
    return python_lines


Count_Py = count_lines_with_python("./text.txt")
print(Count_Py)