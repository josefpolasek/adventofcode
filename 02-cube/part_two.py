import sys

user_input = sys.stdin.read()

sum = 0

for line in user_input.splitlines():
    id, game = line.split(": ")
    id = int(id.split()[-1])
    game = game.split(";")

    possible = True

    red = 0
    green = 0
    blue = 0

    for set in game:
        color = set.split(",")

        for cube in color:
            if cube.split()[1] == "red":
                if (int(cube.split()[0]) > red):
                    red = int(cube.split()[0])
            elif cube.split()[1] == "green":
                if int(cube.split()[0]) > green:
                    green = int(cube.split()[0])
            elif cube.split()[1] == "blue":
                if int(cube.split()[0]) > blue:
                    blue = int(cube.split()[0])
    sum += red*green*blue

print(sum)
