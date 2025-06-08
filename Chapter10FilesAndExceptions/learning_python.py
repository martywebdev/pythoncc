# # Read the file and print the contents by reading the entire file
# with open('learning_python.txt') as file:
#     contents = file.read()
#     print("Reading the entire file:")
#     print(contents)

# # Read the file and print the contents by storing lines in a list and looping
# print("\nReading line by line:")
# with open('learning_python.txt') as file:
#     lines = file.readlines()

# for line in lines:
#     print(line.strip())

from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
lines = contents.splitlines()


# print(contents)
my_string = ''
for line in lines:
    my_string += line
    # print(line)
another_string = my_string.replace('Python', 'C')

print(another_string)