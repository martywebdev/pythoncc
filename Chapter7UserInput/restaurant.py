number_of_people = input('How many people are in your dinner group? ')

if int(number_of_people) > 8:
    print('You will have to wait for a table.')
else:
    print('Your table is ready.')


number = input('Enter a number, and I\'ll tell you if it\'s multiple of 10  : ')

if int(number) % 10 == 0:
    print(f'The number {number} is a multiple of 10.')
else:
    print(f'The number {number} is not a multiple of 10.')


