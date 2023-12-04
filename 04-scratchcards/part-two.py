"""
1 -> 4
2 -> 2
3 -> 2
4 -> 1
5 -> 0
6 -> 0

copies = [1, 2, 4, 8, 14, 1]
"""

import sys
user_input = sys.stdin.read()
lines = user_input.splitlines()

NUMBER_OF_CARDS = 196
cards = [1] * NUMBER_OF_CARDS
    
for id, line in enumerate(lines):
    card, numbers = line.split("|")
    numbers = numbers.split()
    card = card.split(":")[1].split()

    points = 0

    for num in numbers:
        if num in card:
            points += 1
    
    for c in range(1, points+1):
        if id+c >= NUMBER_OF_CARDS:
            break

        cards[id+c] += cards[id]

"""
1 - cards: 2
2 - cards: 6
3 - cards: 18
4 - cards: 42
5 - cards: 1
6 - cards: 1
"""

sum = 0
for id, card in enumerate(cards):
    # print(id+1, "- cards:", card)
    sum += card

# print("sum:", sum)
print(sum)