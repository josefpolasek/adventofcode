import sys
user_input = sys.stdin.read()
lines = user_input.splitlines()

sum = 0
    
for line in lines:
    card, numbers = line.split("|")
    numbers = numbers.split()
    card = card.split(":")[1].split()

    points = 0

    for num in numbers:
        if num in card:
            if (points == 0):
                points = 1
            else:
                points *= 2

    sum += points    

print(sum)
