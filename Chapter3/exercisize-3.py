names = ['eric', 'donna', 'michael', 'steven', 'fez', 'jackie']

for name in names:
    print(f'Hello {name.title()}!')


guests = ['kitty', 'red', 'bob']

for guest in guests:
    print(f'Hi {guest.title()}, I am inviting you to dinner.')


popped = guests.pop(0)

guests.append('midge')

print(f'{popped.title()} can\'t make it to dinner so I\'ll invite {guests[-1].title()} instead')

print(f'My current guests are {', '.join([guest.title() for guest in guests])}')

for guest in guests:
    print(f'Hi {guest.title()}, I am inviting you to dinner.')
