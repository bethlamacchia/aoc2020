"""
part 1: anyone answered yes
part 2: everyone answered yes

"""


if __name__ == "__main__":
    part_1_count, part_2_count = 0, 0
    groups=open("input.txt").read().split("\n\n")
    for entry in groups:
        part_1_count+=len(set(entry.replace("\n", "")))
        part_2_count+=len(set.intersection(*map(set, entry.split())))
    print(part_1_count, part_2_count)



