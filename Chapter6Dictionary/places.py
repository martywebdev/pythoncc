favorite_places = {
    "toto": "singapore",
    "borgmanford": "hongkong",
    "marty": "manila"
}

for person, place in favorite_places.items():
    print(f"{person.title()}'s favorite place is {place.title()}")

favorite_places['mike'] = 'vietnam'

favorite_places.pop('marty')

favorite_places['borgmanford'] = 'isla puting bato  '
print(favorite_places)
