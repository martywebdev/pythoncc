# names = ['eric', 'donna', 'michael', 'steven', 'fez', 'jackie']

# for name in names:
#     print(f'Hello {name.title()}!')

def invitation(guests, message = 'I am inviting you to dinner.'):
    for guest in guests:
        print(f'Hi {guest.title()}, {message}')

guests = ['kitty', 'red', 'bob']

invitation(guests)


popped = guests.pop(0)

guests.append('midge')

print(f'{popped.title()} can\'t make it to dinner so I\'ll invite {guests[-1].title()} instead')

print(f'My current guests are {", ".join([guest.title() for guest in guests])}')

invitation(guests)

additional_guest = ['casey', 'joanne', 'leo']

invitation(guests, 'I found a bigger table!')

guests.insert(0, additional_guest[0])

middle  = round(int(len(guests) / 2) , 2) 

guests.insert(int(middle), additional_guest[1])

guests.append(additional_guest[-1])

invitation(guests)


print('Shame! I can only invite two')

while len(guests) > 2:
    out = guests.pop()
    print(f'Sorry {out.title()} I can\'t invite you to dinner')
print(*guests)

del guests[0]
del guests[0]


print(guests)