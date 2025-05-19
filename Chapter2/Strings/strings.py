message = 'hello world'

print(message)

message = 'New Value for message!'

print(message)

name = 'ada lovelace'

print(name.title())
print(name.upper())
print(name.lower())


first_name = 'marty'
last_name = 'umlas'
full_name = f"{first_name} {last_name}"
print(full_name.title())

#adding white space

print('Python')
print('\tPython')
print('Python\nMachine Learning\n"Double Quoted"\n')
print('\'Single Quoted\'\n"Double Quoted"')

with_white_space = '           Python Crash                                 '
print(with_white_space.rstrip())
print(with_white_space.lstrip())
print(with_white_space.strip())