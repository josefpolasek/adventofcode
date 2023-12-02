def first_digit(strA):
    for i in strA:
        if i.isnumeric():
            return i

def last_digit(strA):
    for i in strA[::-1]:
        if i.isnumeric():
            return i

import sys
user_input = sys.stdin.read()
sum = 0

for line in user_input.splitlines():
    # print(line)
    num = first_digit(line) + last_digit(line)
    sum += int(num)

print (sum)
