from dataclasses import dataclass
import re

with open("input.txt", "r") as file:
    lines = [l.strip() for l in file.readlines()]

cols = len(lines[0])
rows = len(lines)

locs = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


def is_part_number(x: int, y: int) -> bool:
    for dx, dy in locs:
        if x + dx < 0 or x + dx > cols - 1 or y + dy < 0 or y + dy > rows - 1:
            continue

        ch = lines[y + dy][x + dx]
        if not ch.isdigit() and ch != ".":
            return True
    return False


part_numbers = []
for y, line in enumerate(lines):
    for match in re.finditer(r"\d*", line):
        start, end = match.span()

        for x in range(start, end):
            if is_part_number(x, y):
                part_numbers.append(int(line[start:end]))
                break


print("Task 1:", sum(part_numbers))


@dataclass
class Number:
    number: int
    locations: list[tuple[int, int]]

    def __hash__(self):
        return self.number


def find_stars(schematic: list[str]) -> list[tuple[int, int]]:
    star_locs = []
    for y, line in enumerate(schematic):
        for x, ch in enumerate(line):
            if ch == "*":
                star_locs.append((x, y))
    return star_locs


def find_numbers(schematic: list[str]) -> set[Number]:
    numbers: set[Number] = set()
    current_number = ""
    current_locs = []
    for y, line in enumerate(schematic):
        for x, ch in enumerate(line):
            if ch.isdigit():
                current_number += ch
                current_locs.append((x, y))
            else:  # reset
                if current_number != "" and len(current_locs) != 0:
                    numbers.add(
                        Number(number=int(current_number), locations=current_locs)
                    )
                current_number = ""
                current_locs = []

    return numbers


star_locs = find_stars(lines)
numbers = find_numbers(lines)

loc_numbers_map = {}
for number in numbers:
    for loc in number.locations:
        loc_numbers_map[loc] = number.number


def find_surrounding_part_numbers(loc: tuple[int, int]) -> set[int]:
    x, y = loc
    part_numbers = set()

    for dx, dy in locs:
        if number := loc_numbers_map.get((x + dx, y + dy)):
            part_numbers.add(number)

    return part_numbers


gear_ratio_sum = 0
for star_loc in star_locs:
    part_numbers = find_surrounding_part_numbers(star_loc)
    if len(part_numbers) != 2:
        continue
    # print("gear:", star_loc)
    gear_ratio = 1
    for part_number in part_numbers:
        gear_ratio *= part_number

    gear_ratio_sum += gear_ratio

print("Task 2:", gear_ratio_sum)
