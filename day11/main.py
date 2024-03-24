from typing import Iterator
from itertools import combinations

with open("input.txt") as file:
    lines = file.read().splitlines()

type Coordinates = tuple[int, int]  # x, y


class Array2D:
    def __init__(self, data: list[list[str]]) -> None:
        self._data = data
        self.n_rows = len(data)
        self.n_cols = len(data[0])

    def get_row(self, row: int) -> list[str]:
        return self._data[row]

    def get_col(self, column: int) -> list[str]:
        return [row[column] for row in self._data]

    def get_value(self, row: int, column: int) -> str:
        return self._data[row][column]

    def iterrows(self) -> Iterator[list[str]]:
        for row in self._data:
            yield row

    def itercols(self) -> Iterator[list[str]]:
        for column in range(len(self._data[0])):
            yield self.get_col(column)

    def insert_row(self, row: int, values: list[str]) -> None:
        if len(values) != self.n_cols:
            raise ValueError("The number of values must match the number of columns.")
        self._data.insert(row, values)
        self.n_rows += 1

    def insert_col(self, column: int, values: list[str]) -> None:
        if len(values) != self.n_rows:
            raise ValueError("The number of values must match the number of rows.")
        for i, value in enumerate(values):
            self._data[i].insert(column, value)
        self.n_cols += 1

    def __str__(self) -> str:
        return "\n".join("".join(row) for row in self._data)


def find_empty_rows(array: Array2D, empty_value: str = ".") -> list[int]:
    empty_rows = []
    for i, row in enumerate(array.iterrows()):
        if set(row) == {empty_value}:
            empty_rows.append(i)
    return empty_rows


def find_empty_columns(array: Array2D, empty_value: str = ".") -> list[int]:
    empty_columns = []
    for i, column in enumerate(array.itercols()):
        if set(column) == {empty_value}:
            empty_columns.append(i)
    return empty_columns


def find_galaxies(array: Array2D, galaxy_value: str = "#") -> set[Coordinates]:
    galaxies = set()
    for i, row in enumerate(array.iterrows()):
        for j, value in enumerate(row):
            if value == galaxy_value:
                galaxies.add((i, j))
    return galaxies


def manhattan_distance(p1: Coordinates, p2: Coordinates) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


image = Array2D([list(line) for line in lines])


empty_rows = find_empty_rows(image)
for i, row in enumerate(empty_rows):
    image.insert_row(row, ["." for _ in range(image.n_cols)])
    for j in range(i + 1, len(empty_rows)):
        empty_rows[j] += 1

empty_cols = find_empty_columns(image)
for i, col in enumerate(empty_cols):
    image.insert_col(col, ["." for _ in range(image.n_rows)])
    for j in range(i + 1, len(empty_cols)):
        empty_cols[j] += 1


galaxies = find_galaxies(image)

galaxy_pairs = combinations(galaxies, 2)

distances = {pair: manhattan_distance(*pair) for pair in galaxy_pairs}

sum_distances = sum(distances.values())

print(sum_distances)
