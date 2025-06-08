from pathlib import Path

# # Get the directory where the script is located
# script_dir = Path(__file__).parent
# # Create path to the pi_digits.txt file in the same directory as the script
# path = script_dir / 'pi_digits.txt'
# contents = path.read_text()
# print(contents)

path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))


birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

    