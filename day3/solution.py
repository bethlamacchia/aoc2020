import math

"""
For part 2:
Find the product of the num. trees hit with slopes of
    Right 1, down 1.
    Right 3, down 1. (This is the slope from part1.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

"""

def trees_hit(lines):
    x = 3
    y = 1
    trees = 0
    while y < len(lines):
        if x > len(lines[y]) - 1:
            x = x % len(lines[y])
        if lines[y][x] == '#':
            trees += 1
        x += 3
        y += 1
    return trees

with open('input.txt') as file:
    lines = [line for line in file]
    height = len(lines)
    width = len(lines[0])
    lines = [list(line.rstrip()) for line in lines]

    print("Part 1", trees_hit(lines))


