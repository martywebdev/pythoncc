for i in range(1, 21):
    print(i)

# numbers = []

# for i in range(1, 1000000):
#     numbers.append(i)
# print(numbers)

numbers = list(range(1, 1_000_001))  # list comprehensions

print(min(numbers))
print(max(numbers))


peoples = ['john', 'paul', 'george', 'ringo']

x = ','.join(people for people in peoples)

print(x)

print(sum(numbers))

print([odd for odd in range(1, 20, 2)])

print([three for three in range(1, 30, 3)])


print([cube ** 3 for cube in range(1, 10)])
