from collections import defaultdict
"""
part 1:
Simulate your seating area by applying the seating rules repeatedly until no seats change state. 
How many seats end up occupied?

part 2:
Now, instead of considering just the eight immediately adjacent seats,
consider the first seat in each of those eight directions (ie, doesn't have to be adjacent).

it now takes five or more visible occupied seats for an occupied seat to become empty
(rather than four or more from the previous rules). 
The other rules still apply: empty seats that see no occupied seats become occupied, 
seats matching no rule don't change, and floor never changes. 
"""

def count_adj(row,col,prev, part_one):
    s=0
    for rinc,colinc in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        r=row
        c=col
        while True:
            r=r+rinc
            c=c+colinc
            if(r<0 or r>=len(prev)) or (c<0 or c>=len(prev[row]) or prev[r][c]=="L"):
                break
            if(prev[r][c]=="#"):
                s+=1
                break
            # for part one we only look at immediately adjacent seats so break after one step
            # in each direction,
            # for part 2 keep going in each direction until we hit an occupied seat
            # or a wall
            if (part_one):
                break
    return s

def solve(data, part_one):
    table=[row.copy() for row in data]
    # each calculation should be based off of the unchanged seats, even though
    # we change the seating as we go through the table, so make a copy
    while True:
        prev = [row.copy() for row in table]
        # look at each seat, using prev to look at seats before we started the simulation in this round
        for row in range(len(table)):
            for col in range(len(table[row])):
                # if this isn't a floor space (.)
                if(table[row][col]!="."):
                    # count how many adjacent seats are filled
                    n=count_adj(row, col, prev, part_one)
                    # if no seats filled adjacent and this is an empty seat,fill the seat
                    if(n==0 and prev[row][col]=="L"):
                        table[row][col]="#"
                    # if more than 4 seats filled adjacent and this is a filled seat, vacate it
                    # part 2: five visible seat
                    if(n>=(4 if part_one else 5)and prev[row][col]=="#"):
                        table[row][col]="L"
        if prev==table:
            break
    # count the filled seats
    return "\n".join(["".join(row)for row in table]).count("#")

if __name__ == "__main__":

    data = open("input.txt", "r").read().strip().split("\n")
    data = [list(row) for row in data]
    print("Part 1: ", solve(data, part_one=True))
    print("Part 2: ", solve(data, part_one=False))

