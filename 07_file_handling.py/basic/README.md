File handling in Python involves reading from and writing to files on your computer. Python provides built-in functions and methods for file handling operations.

Here's a basic overview of file handling operations in Python:

1. **Opening a File**: You can open a file using the built-in `open()` function. It takes two arguments: the file path and the mode in which you want to open the file (read, write, append, etc.).

   ```python
   file = open("example.txt", "r")  # Opens the file in read mode
   ```

2. **Reading from a File**: You can read the contents of a file using various methods like `read()`, `readline()`, or `readlines()`.

   ```python
   content = file.read()  # Reads the entire content of the file
   ```

3. **Writing to a File**: You can write data to a file using the `write()` method.

   ```python
   file = open("example.txt", "w")  # Opens the file in write mode
   file.write("Hello, World!")  # Writes the string to the file
   ```

4. **Appending to a File**: You can append data to an existing file using the `a` mode or `append()` method.

   ```python
   file = open("example.txt", "a")  # Opens the file in append mode
   file.write("\nAppending new data!")  # Appends the string to the file
   ```

5. **Closing a File**: After performing file operations, it's important to close the file using the `close()` method to free up system resources.

   ```python
   file.close()  # Closes the file
   ```

6. **Using Context Managers (Recommended)**: You can use the `with` statement as a context manager to automatically close the file after execution, ensuring cleaner and safer code.

   ```python
   with open("example.txt", "r") as file:
       content = file.read()
   ```

7. **File Handling Modes**:
   - `"r"`: Read mode (default). Opens the file for reading.
   - `"w"`: Write mode. Opens the file for writing. If the file doesn't exist, it creates a new file. If the file exists, it truncates the file.
   - `"a"`: Append mode. Opens the file for appending. If the file doesn't exist, it creates a new file.
   - `"r+"`: Read and write mode. Opens the file for both reading and writing.

These are the basic operations involved in file handling in Python. Make sure to handle exceptions and errors appropriately while working with files. Additionally, always close the files after usage to avoid memory leaks.
