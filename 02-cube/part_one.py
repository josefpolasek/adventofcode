import sys
user_input = sys.stdin.read()

red = 12
green = 13
blue = 14

sum = 0

for line in user_input.splitlines():
    id, game = line.split(": ")
    id = int(id.split()[-1])
    game = game.split(";")

    possible = True

    for set in game:
        color = set.split(",")
        
        for cube in color:
            if (cube.split()[1] == "red"):
                if (int(cube.split()[0]) >  12):
                    possible = False
            elif (cube.split()[1] == "green"):
                if (int(cube.split()[0]) >  13):
                    possible = False
            elif (cube.split()[1] == "blue"):
                if (int(cube.split()[0]) >  14):
                    possible = False
    
    if (possible):
        sum += id
    
print (sum)
