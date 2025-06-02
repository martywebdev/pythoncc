usernames = ['admin', 'martyweb', 'user1', 'user2', 'user3']
if usernames:
    for index, user in enumerate(usernames):
        if user == 'admin':
            print(
                f'{index + 1}. Hello {user.title()} this is a special greeting')
        else:
            print(
                f'{index}. Hi {user.title()} this is a greeting for a peasant.')
else:
    print('We need to find users!!!')


current_users = ['steven', 'michael', 'eric', 'fez', 'PETE']

new_users = ['john', 'paul', 'george', 'ringo', 'Pete']


for user in new_users:
    if user.lower() in [current_user.lower() for current_user in current_users]:
        print(f'{user} was already used')

numbers = []

numbers.extend(num for num in range(1, 900))

# for num in numbers:
#     if num == 1:
#         print(f'{num}st')
#     elif num == 2:
#         print(f'{num}nd')
#     elif num == 3:
#         print(f'{num}rd')
#     else:
#         print(f'{num}th')


for num in numbers:
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(num % 10, 'th')
    print(f'{num}{suffix}')