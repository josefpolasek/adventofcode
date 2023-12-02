def first_digit(strA):
    for i in strA:
        if i.isnumeric():
            return i


numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
# print(numbers.index("nine")) -> 9


def find_all_occurrences(substring, input_string):
    indexes = []
    start_index = 0

    while True:
        index = input_string.find(substring, start_index)

        if index == -1:
            break  # No more occurrences found
        else:
            indexes.append(index)
            start_index = index + 1

    return indexes


def find_number(input_string):
    num = []

    # finds all numbers in decimal form (1, 2, 3)
    for i in input_string:
        if i.isnumeric():
            num.append(i)

    # numbers in words (one, two, three)
    for i in numbers:
        if i in input_string:
            num.append(i)

    # print(num)

    # find first number
    first = num[0]
    for n in num:
        if input_string.index(n) < input_string.index(first):
            first = n
    # make a number
    if not first.isnumeric():
        first = numbers.index(first)
    else:
        first = int(first)

    # print("first:", first)

    # find last number
    last_index = 0
    last = num[0]

    for n in num:
        indexes = find_all_occurrences(n, input_string)

        for i in indexes:
            if i > last_index:
                last_index = i
                last = n

    # make a number
    if not last.isnumeric():
        last = numbers.index(last)
    else:
        last = int(last)

    # print("last:", last)

    result = int(str(first) + str(last))

    return result


def last_digit(strA):
    for i in strA[::-1]:
        if i.isnumeric():
            return i


import sys

user_input = sys.stdin.read()
sum = 0

for line in user_input.splitlines():
    # print(line)
    # print(find_number(line))

    sum += find_number(line)

print(sum)
