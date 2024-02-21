# Open file in append mode to add new tasks
file = open('E:/#LearningPython/07_file_handling.py/02_todo.txt', 'a')

# Take input from the user for the task
task = input('Enter the task you want to store: ')

# Write the task along with a sequential number to the file
# Increment the count for each new task
with open('E:/#LearningPython/07_file_handling.py/02_todo.txt', 'r') as f:
    count = sum(1 for _ in f) + 1  # Get the number of existing tasks
file.write(f'{count}) {task}\n')

# Close the file
file.close()

# Open file in read mode to display the content
file = open('E:/#LearningPython/07_file_handling.py/02_todo.txt', 'r')

# Read the content of the file
content = file.read()

# Close the file
file.close()

# Print the content
print("Current Tasks:")
print(content)




