with open("input.txt", "r") as file:
    lines = [l.strip() for l in file.readlines()]


def parse_line(line: str) -> tuple[int, list[dict[str, int]]]:
    game_str, subsets_str = line.split(": ")
    game_id = int(game_str.split()[-1])

    subsets = []
    for subset_str in subsets_str.split("; "):
        subset = {}
        for cubes in subset_str.split(", "):
            n, color = cubes.split()
            subset[color] = int(n)

        subsets.append(subset)

    return game_id, subsets


def is_possible(subsets: list[dict[str, int]]) -> bool:
    bag = {"red": 12, "green": 13, "blue": 14}
    for subset in subsets:
        for color, n in subset.items():
            if bag[color] < n:
                return False
    return True


sum_possible_ids = 0
for line in lines:
    possible = True

    game_id, subsets = parse_line(line)
    # print(game_id, subsets)

    if is_possible(subsets):
        sum_possible_ids += game_id

print("Task 1:", sum_possible_ids)


power_sum = 0
for line in lines:
    game_id, subsets = parse_line(line)

    rgb_min: dict[str, int] = {}

    for subset in subsets:
        for color, n in subset.items():
            if color not in rgb_min.keys():
                rgb_min[color] = n
            else:
                if n > rgb_min[color]:
                    rgb_min[color] = n

    power = 1
    for n in rgb_min.values():
        power *= n

    power_sum += power

print("Task 2:", power_sum)
