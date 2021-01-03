

"""
part 1:
What is the ID of the earliest bus you can take to the airport
multiplied by the number of minutes you'll need to wait for that bus?

Part 2
What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list?
An x in the schedule means there are no constraints on what bus IDs must depart at that time.
** had to use hint ("Chinese Remainder Theorem" was required)
All bus IDs are prime - greatest common divisor will always be 1
"""

def part_one(timestamp, ids):
    buses = [int(i) for i in ids if i != 'x']
    wait_times = []
    for bus in buses:
        prev_bus = timestamp // bus * bus
        wait_times.append(prev_bus + bus - timestamp)
    return min(wait_times) * buses[wait_times.index(min(wait_times))]

# least common multiple of matched buses
def compute_lcm(a):
    # first bus in the list
    lcm = a[0]
    # for rest of bus intervals
    for i in a[1:]:
        # prime nums - greatest common divisor is going to be 1
        lcm = lcm * i
    return lcm

# first line is no longer relevant
def part_two(ids):
    buses = []
    for bus in ids:
        buses.append(int(bus)) if bus != 'x' else buses.append('x')
    timestamp = 0
    matched_buses = [buses[0]]
    while True:
        timestamp += compute_lcm(matched_buses)
        # print(timestamp)
        for i, bus in enumerate(buses):
            if bus != 'x':
                # buses need to depart sequentially
                if (timestamp + i) % bus == 0:
                    if bus not in matched_buses:
                        matched_buses.append(bus)
        if len(matched_buses) == len(buses) - buses.count('x'):
            break

    return timestamp


if __name__ == "__main__":
    with open('input.txt') as f:
        inp = f.readlines()
        # earliest time you can depart on a bus
        timestamp = int(inp[0])
        # ids in service
        # each id indicates how often the bus leaves, starting at time 0
        ids = inp[1].split(',')
        print("Part 1: ", part_one(timestamp, ids))
        print("Part 2: ", part_two(ids))



