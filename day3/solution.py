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

p2_right = [1, 3, 5, 7, 1]
p2_down = [1, 1, 1, 1, 2]

def trees_hit(x, y, lines):
    dx = x
    dy = y
    trees = 0
    while y < len(lines):
        if x > len(lines[y]) - 1:
            x = x % len(lines[y])
        if lines[y][x] == '#':
            trees += 1
        x += dx
        y += dy
    return trees

with open('input.txt') as file:
    lines = [line for line in file]
    height = len(lines)
    width = len(lines[0])
    lines = [list(line.rstrip()) for line in lines]

    print("Part 1", trees_hit(3, 1, lines))

    tree_product = 1
    for (x, y) in zip(p2_right, p2_down):
        tree_product *= trees_hit(x, y, lines)

    print("Part 2", tree_product)


