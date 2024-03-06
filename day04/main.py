import re

with open("input.txt", "r") as file:
    lines = [l.strip() for l in file.readlines()]


pattern = r"\d+"
r = re.compile(pattern)

card_counter = [1] * len(lines)
for i, line in enumerate(lines):
    numbers_str = line.split(":")[1].split("|")

    winning_numbers = r.findall(numbers_str[0])
    numbers = r.findall(numbers_str[1])

    intersection = set(numbers).intersection(winning_numbers)

    for j in range(len(intersection)):
        # for each of the next #wins cards
        # add 1 count for each existing current card
        card_counter[i + j + 1] += card_counter[i]

total_cards = sum(card_counter)
print("Task 2:", total_cards)
