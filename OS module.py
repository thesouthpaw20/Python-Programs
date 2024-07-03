import os

# Create a directory
dir_name = "test_directoryh"
os.mkdir(dir_name)
print(f"Directory '{dir_name}' created.")

# Directory listing
print("Directory listing:")
print(os.listdir('.'))

# Search for .py files
print("Python files in directory:")
for file in os.listdir('.'):
    if file.endswith('.py'):
        print(file)

# Remove a particular file
file_to_remove = input("Enter the file name to remove: ")
if os.path.exists(file_to_remove):
    os.remove(file_to_remove)
    print(f"File '{file_to_remove}' removed.")
else:
    print(f"File '{file_to_remove}' not found.")
