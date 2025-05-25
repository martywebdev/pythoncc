pizzas = ['hawaian', 'italian', 'sicilian']

for pizza in pizzas:
    print(f'I like {pizza.title()} pizza')
print('I really love pizza  ')


animals = ['cat', 'dog', 'mouse']

print(f'{", ".join([animal.lower() for animal in animals])}')

for animal in animals:
    remark = f'A {animal} would make a good pet'
    # print(remark if animal == 'dog' else '')
    print(remark)
print('Any of these animals would make a great pet!')
