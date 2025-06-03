person = {
    'name': 'dianne',
    'job': 'lawyer'
}

person_numbers = {
    'jawo': 7,
    'fernandez': 10,
    'jordan': 23,
    'pippen': 33,
    'ewing': 33
}


for k, v in person_numbers.items():
    print(f"{k.title()}'s favarite number is {v}")


portfolio_architecture = {
    'frontend': 'blade and alpine',
    'backend': 'inertia and react',
    'database': 'mysql',
    'server': 'digital ocean',
    'email': 'zoho',
    'test': 'phpunit',
    'test': 'zen'
}

# for item in portfolio_architecture.keys():
#     print(f'{item}')

# if 'test' not in portfolio_architecture.keys():
#     print(f'testing is not included')
# else:
#     print(f'its included')


for item in sorted(portfolio_architecture.keys()):
    print(item)

for item in sorted(portfolio_architecture.values()):
    print(item)

for item in set(portfolio_architecture.keys()):
    print(item)
