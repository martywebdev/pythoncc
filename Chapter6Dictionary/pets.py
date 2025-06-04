pets = [
    {
        "animal": "dog",
        'owner': 'toto'
    },
    {
        'animal': 'cat',
        'owner': 'borgmanford'
    }
]

for pet in pets:
    print(f"{pet['owner'].title()} has a pet {pet['animal']}")
