alien_0 = {
    'color': 'green',
    'points': 5
}

print(alien_0)
alien_0['x_position'] = 0

print(alien_0)
alien_0['color'] = 'red'

print(alien_0)


del alien_0['points']

print(alien_0)
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")


print(alien_0.get('points', 'No points'))
