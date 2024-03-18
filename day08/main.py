import re

with open("input.txt", "r") as file:
    lines = file.read().split("\n")


class Node:
    def __init__(self, name: str, left: str, right: str):
        self.name = name
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{self.name} = ({self.left}, {self.right})"


def parse_nodes(lines: list[str]) -> dict[str, Node]:
    nodes = {}
    pattern = re.compile(r"\w+")

    for line in lines:
        name, left, right = tuple(pattern.findall(line))
        nodes[name] = Node(name, left, right)

    return nodes


def find_path(start: str, end: str, nodes: dict[str, Node], instructions: str):
    current = nodes[start]
    steps = 0

    while current.name != end:
        instruction = instructions[steps % len(instructions)]
        if instruction == "L":
            current = nodes[current.left]
        else:
            current = nodes[current.right]
        steps += 1

    return steps

start = "AAA"
end = "ZZZ"

instructions = lines[0]
nodes = parse_nodes(lines[2:-1])

result = find_path(start, end, nodes, instructions)
print(result)
