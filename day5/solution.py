"""
this is essentially binary space partitioning

"""


if __name__ == "__main__":
    seats=[]
    # transform to binary
    for line in open('input.txt'):
        binary_seat = int((line.replace('B', '1').replace('F', '0')
             .replace('R', '1').replace('L', '0')), 2)
        seats.append(binary_seat)
    min, max = min(seats), max(seats)
    # part 1
    print(max)
    # part 2
    for s in range(min, max):
        if s not in seats:
            print(s)

