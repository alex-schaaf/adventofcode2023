import re
import math

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


def task1(instructions, nodes) -> int:
    start = "AAA"
    end = "ZZZ"

    instructions = lines[0]
    nodes = parse_nodes(lines[2:-1])

    result = find_path(start, end, nodes, instructions)
    return result


instructions = lines[0]
nodes = parse_nodes(lines[2:-1])

print("Task 1:", task1(instructions, nodes))


def task2(instructions: str, nodes: dict[str, Node]) -> int:
    """
    Using the same logic as in task1, we can find the number of steps it takes
    for each start not to reach its respective end node. So for each start node
    we have this cycle number. We then need to find the lowest common multiple
    (LCM), as thats the number of steps when all cycles are in sync.

    Example:

    Starting with 2 nodes, A and B, one with cycle 2 and one with cycle 3, the
    LCM is 6.

       1 2  3  4  5 6
    A [x x][x  x][x x] (cycle 2)
    B [x x  x][x  x x] (cycle 3)
    """
    start_nodes = [n for n in nodes.values() if n.name.endswith("A")]
    node_cycles = []

    for current in start_nodes:
        steps = 0
        while not current.name.endswith("Z"):
            instruction = instructions[steps % len(instructions)]
            if instruction == "L":
                current = nodes[current.left]
            else:
                current = nodes[current.right]
            steps += 1

        node_cycles.append(steps)

    return math.lcm(*node_cycles)


print("Task 2:", task2(instructions, nodes))
