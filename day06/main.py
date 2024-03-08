from functools import reduce
import matplotlib.pyplot as plt
import numpy as np

with open("input.txt", "r") as file:
    lines = file.readlines()

times = map(int, lines[0].split(":")[1].split())
best_distances = map(int, lines[1].split(":")[1].split())


def calc_distance(total_time: int, charging_time: int) -> int:
    return (total_time - charging_time) * charging_time


def task1():
    n_record_breakers = []
    for total_time, best_distance in zip(times, best_distances):
        runs = []
        for charging_time in range(1, total_time):
            distance = calc_distance(total_time, charging_time)
            runs.append(distance)

        record_breakers = filter(
            lambda run_distance: run_distance > best_distance, runs
        )
        n_record_breakers.append(len(list(record_breakers)))

    product = reduce(lambda x, y: x * y, n_record_breakers)
    print("Task 1:", product)


# task1()


def task2():
    time = int("".join(map(str, times)))
    best_distance = int("".join(map(str, best_distances)))
    print(time, best_distance)

    count = 0
    for t in range(time):
        distance = calc_distance(time, t)
        if distance > best_distance:
            count += 1

    print("Task 2:", count)


task2()
