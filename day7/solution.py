import re
from collections import defaultdict
"""
parsing, dependency graphs
part 1: how  many bags could contain at least one shiny gold bag?
part 2: How many individual bags are required inside a single shiny gold bag?
"""

if __name__ == "__main__":

    bags = defaultdict(dict)
    with open("input.txt") as file:
        for line in file:
            # get just the color of the outer bag, ie "shiny gold"
            bag = re.match(r'(.*) bags contain', line).groups()[0]
            # construct the graph
            # re.findall(r'(\d+) (\w+ \w+) bag', line) gets all of that bag's dependencies,
            # for example [('5', 'shiny magenta'), ('1', 'dotted orange'), ('2', 'wavy teal')]
            for count, color in re.findall(r'(\d+) (\w+ \w+) bag', line):
                # append each color and count as a dependency of the current color bag
                bags[bag][color] = int(count)
    # want unique num of bags - use a set
    part_one_bags = set()
    def total_color_bags(color):
        for b in bags:
            if color in bags[b]:
                # recursively search through the bags
                part_one_bags.add(b)
                total_color_bags(b)
    total_color_bags('shiny gold')
    print(len(part_one_bags))

    def total_num_bags(bag):
        count = 1
        for s in bags[bag]:
            # include respective total bags of each bag inside this bag
            multiplier = bags[bag][s]
            count += multiplier * total_num_bags(s)
        return count

    print(total_num_bags('shiny gold') - 1)  # subtract one for shiny gold itself
