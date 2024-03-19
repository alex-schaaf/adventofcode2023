with open("input.txt", "r") as file:
    lines = file.readlines()

histories = [list(map(int, line.split())) for line in lines]


def diff(arr: list[int]) -> list[int]:
    return [arr[i] - arr[i - 1] for i in range(1, len(arr))]


def extrapolate(arr: list[int], previous_value: int = 0) -> int:
    if set(arr) == set([0]):
        return previous_value
    return extrapolate(diff(arr), previous_value + arr[-1])


print("Task 1:", sum((extrapolate(history) for history in histories)))
print("Task 2:", sum((extrapolate(history[::-1]) for history in histories)))
