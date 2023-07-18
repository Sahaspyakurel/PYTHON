def time(n):
    lap_times = []
    for lap in range(1, n + 1):
        time = float(input(f"Enter the lap time for lap {lap}: "))
        lap_times.append(time)

    fastest_lap = lap_times[0]
    for time in lap_times:
        if time < fastest_lap:
            fastest_lap = time

    slowest_lap = lap_times[0]
    for time in lap_times:
        if time > slowest_lap:
            slowest_lap = time

    lap_sum = 0
    for time in lap_times:
        lap_sum += time
    average_lap = lap_sum / n

    print(f"Fastest Lap Time: {fastest_lap:.2f}")
    print(f"Slowest Lap Time: {slowest_lap:.2f}")
    print(f"Average Lap Time: {average_lap:.2f}")

num_laps = int(input("Enter the number of times you have run around the racetrack: "))
time(num_laps)
