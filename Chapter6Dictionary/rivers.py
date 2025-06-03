rivers = {
    'nile': 'egypt',
    'pasig river': 'philippines',
    'missisippi': 'usa'
}

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}')


print("These are the river names")
for river in rivers.keys():
    print(river.title())

print('These are names of the countries')
for country in rivers.values():
    print(country.title())
