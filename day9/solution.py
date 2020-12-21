
"""
part 1:
find the first number in the list (after the preamble) which is not the sum of two of the 25 numbers before it.
 What is the first number that does not have this property?

part 2:
 find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.
add together the smallest and largest number in this contiguous range.
"""

def valid_number(window, number):
    for n in window:
        dif = abs(number-n)
        if n != dif and dif in window: return True
    return False

def part1(input):
    # start with the first 25 nums
    window = input[:25]
    i = 1
    for number in input[25:]:
        if not valid_number(window, number):
            return number
        else:
            # move the window over by 1
            window = input[i:25+i]
            i += 1
    return False


def find_contiguous(nums, target):
    for i in range(0, len(nums)-1):
        for j in range(i, len(nums)):
            if sum(nums[k] for k in range(i, j)) == target:
                return nums[i:j]

if __name__ == "__main__":

    with open("input.txt") as file:
        lines = file.readlines()
    nums = list(map(int, lines))
    part1 = part1(nums)
    print("Part 1: " + str(part1))
    part2_nums = find_contiguous(nums, part1)
    print("Part 2: " + str(max(part2_nums) + min(part2_nums)))
