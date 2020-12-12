
with open('input.txt') as file:
    letters = [num.split(": ") for num in file]
    part1_tally, part2_tally = 0, 0
    for policy, password in letters:
        length, letter = policy.split(" ")
        start, stop = length.split("-")
        start, stop = int(start), int(stop)

        # part 1
        if start <= password.count(letter) <= stop: part1_tally += 1

        # part 2: Only exactly one of these positions must contain the given letter -> XOR
        # indexes start at 1 so need to shift everything by 1
        if (password[start - 1] == letter) ^ (password[stop - 1] == letter):
            part2_tally += 1

    print("Part 1:", part1_tally)
    print("Part 2:", part2_tally)
