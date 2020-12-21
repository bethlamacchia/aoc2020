from collections import defaultdict
"""
part 1:
What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?

part 2:
What is the total number of distinct ways you can 
arrange the adapters to connect the charging outlet to your device?

"""

if __name__ == "__main__":

    with open("input.txt") as fileinput:

        # sort the list of adapters
        adapters = [0] + sorted(map(int, fileinput))

        # our built-in joltage adapter rates 3 jolts higher
        # than the highest-rated adapter in the list
        adapters.append(adapters[-1] + 3)

        # store the counts of difs
        diffs = defaultdict(int)
        # store number of ways to reach this adapter
        counts = defaultdict(int, {0: 1})

        for a, b in zip(adapters[1:], adapters):
            diffs[a - b] += 1
            # number of ways to reach i'th adapter from previous three
            counts[a] = counts[a - 3] + counts[a - 2] + counts[a - 1]

    print("Part 1: " + str(diffs[1] * diffs[3]))
    print("Part 2: " + str(counts[adapters[-1]]))
