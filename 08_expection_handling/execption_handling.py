# 1. try-except block: This is the basic structure for handling exceptions in Python. Code that might raise an exception is placed within the `try` block, and any exceptions that occur are caught and handled in the `except` block.

try:
    # Code that might raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Handle the exception
    print("Error: Division by zero")
   

# 2. Multiple except blocks: You can have multiple `except` blocks to handle different types of exceptions.
try:
        # Code that might raise an exception
    result = int("hello")  # This will raise a ValueError
except ValueError:
        # Handle ValueError
    print("Error: Invalid conversion")
except TypeError:
        # Handle TypeError
    print("Error: Type mismatch")


# 3. else block: The `else` block is executed if no exceptions are raised within the `try` block.

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print("Result:", result)


# 4. finally block: The `finally` block is always executed, regardless of whether an exception occurred or not. It's commonly used for cleanup operations.

try:
    f = open("myfile.txt", "r")
    # Perform file operations
except FileNotFoundError:
    print("Error: File not found")
finally:
    # Close the file, regardless of whether an exception occurred or not
    f.close()


# 5.Raising exceptions: You can manually raise exceptions using the `raise` statement.
x = -1
if x < 0:
    raise ValueError("Negative numbers are not allowed")

