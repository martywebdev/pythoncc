players = ['charles', 'martina', 'michael', 'florence', 'eli']


print(players[:])
print(players[:1])
print(players[1:2])
print(players[1:3])
print(players[:-1])
print(players[len(players)-1:])
print(players[-1])

for player in players[:3]:
    print(player.title())

print(len(players) / 2)

print(players[round(len(players) / 2) : ])

   