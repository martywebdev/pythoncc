people = [
    {
        "name": 'toto',
        "job": "programmer"
    },

    {
        "name": "borgmanford",
        'job': "trader"
    }
]

for index, person in enumerate(people):
    print(f'{index}: {person["name"]} is a {person["job"]}')

for person in people:
   print(f"{person['name']}")
