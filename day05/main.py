with open("input.txt", "r") as file:
    lines = [l.strip() for l in file.readlines()]


def parse(lines: list[str]) -> dict[str, list[tuple[int, int, int]]]:
    categories = {}

    for line in lines[2:]:
        if len(line) == 0:
            continue
        elif line[0].isalpha():
            category = line.split()[0]
            categories[category] = []
        elif line[0].isdigit():
            start_dest, start_source, length = (int(i) for i in line.split())
            categories[category].append((start_dest, start_source, length))
    return categories


seeds = [int(s) for s in lines[0].split(":")[1].split()]
categories = parse(lines)


def task1():
    locations = []
    for value in seeds:
        source_key = "seed"
        destination_key = None

        while destination_key != "location":
            category_key = next(
                filter(lambda key: key.startswith(source_key), categories.keys())
            )
            destination_key = category_key.split("-")[-1]

            for range_ in categories[category_key]:
                start_dest, start_source, length = range_
                if start_source <= value <= start_source + length:
                    value = start_dest + abs(start_source - value)
                    break

            source_key = destination_key

        locations.append(value)

    print("Task 1:", min(locations))


task1()
