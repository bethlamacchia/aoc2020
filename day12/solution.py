"""
part 1:
Figure out where the navigation instructions lead.
What is the Manhattan distance between that location and the ship's starting position?

part 2:
now moving the waypoint; Action F means to move forward to the waypoint the given number of times.
What is the Manhattan distance between that location and the ship's starting position?
"""

def direction_helper(dir):
    if dir >= 0:
        return dir % 360
    else:
        return 360 + dir


def solution(part_two=False):
    dir = 90
    ship_ew = 0
    ship_ns = 0
    way_ew = 10
    way_ns = 1

    with open('input.txt') as inp:
        for line in inp:
            action, num = line[0], int(line[1:])
            if part_two:
                if action == "F":
                    ship_ns += (way_ns * num)
                    ship_ew += (way_ew * num)
                elif action == "N":
                    way_ns += num
                elif action == "S":
                    way_ns -= num
                elif action == "E":
                    way_ew += num
                elif action == "W":
                    way_ew -= num

                elif action == "L" and num == 90 or action == "R" and num == 270:
                    way_ns, way_ew = way_ew, -way_ns
                elif action == "L" and num == 270 or action == "R" and num == 90:
                    way_ns, way_ew = -way_ew, way_ns
                elif action == "L" and num == 180 or action == "R" and num == 180:
                    way_ns = -way_ns
                    way_ew = -way_ew
            else: # part one
                if action == "F" and dir == 90 or action == "E":
                    ship_ew += num
                elif action == "F" and dir == 180 or action == "S":
                    ship_ns -= num
                elif action == "F" and dir == 270 or action == "W":
                    ship_ew -= num
                elif action == "F" and dir == 0 or action == "N":
                    ship_ns += num
                elif action == "L":
                    dir -= num
                    dir = direction_helper(dir)

                elif action == "R":
                    dir += num
                    dir = direction_helper(dir)

        return abs(ship_ns) + abs(ship_ew)


if __name__ == "__main__":
    print("Part 1 Manhattan distance: " + str(solution()))
    print("Part 2 Manhattan distance: " + str(solution(part_two=True)))



