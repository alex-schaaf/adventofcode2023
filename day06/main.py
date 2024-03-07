from functools import reduce

with open("input.txt", "r") as file:
    lines = file.readlines()

times = map(int, lines[0].split(":")[1].split())
best_distances = map(int, lines[1].split(":")[1].split())
acceleration = 1

#
#


n_record_breakers = []
for time, best_distance in zip(times, best_distances):
    runs = []
    for charging_time in range(1, time):
        speed = charging_time
        travel_time = time - charging_time
        distance = travel_time * speed
        runs.append(distance)

    record_breakers = filter(lambda run_distance: run_distance > best_distance, runs)
    n_record_breakers.append(len(list(record_breakers)))

product = reduce(lambda x, y: x * y, n_record_breakers)
print("Task 1:", product)
