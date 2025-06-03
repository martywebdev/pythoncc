places_to_visit = ['hongkong', 'usa', 'spain', 'france', 'italy']

print(f'original list {places_to_visit}')


temp = sorted(places_to_visit)

print(f'sorted list alphabetical temp {temp}')


temp_reverse = sorted(places_to_visit, reverse=True)

print(f'sorted list reverse {temp_reverse}')

print(f'original list {places_to_visit}')

places_to_visit.reverse()
print(f'original list reversed {places_to_visit}')
places_to_visit.reverse()
print(f'back to original {places_to_visit}')
places_to_visit.sort()
print(f'original list sorted alphabetically {places_to_visit}')
print(f'reversed alphabetical {sorted(places_to_visit, reverse=True)}')
