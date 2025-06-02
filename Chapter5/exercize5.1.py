requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")


numbers = range(1, 10)

for number in numbers:
    if 1 in numbers:
        print('yo')
        break
    else:
        print('nay')
