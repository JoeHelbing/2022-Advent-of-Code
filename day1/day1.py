import numpy as np

class ElfBag:
    def __init__(self):
        self.contents = None
        self.total = None


    def __repr__(self):
        return f"ElfBag has: {self.contents} \n Total: {self.total}"


    def add(self, other):
        #add new item to elf bag
        if self.contents is None:
            self.contents = [other]
            self.total = other
        else:
            self.contents.append(other)
            self.total = sum(self.contents)
        return None


def biggest_bag(bags):
    """Return the bag with the highest total"""
    return max(bags, key=lambda bag: bag.total)


def three_biggest_bags(bags):
    """Return the three bags with the highest total"""
    big_bags = sorted(bags, key=lambda bag: bag.total, reverse=True)[:3]
    sum = 0
    for bag in big_bags:
        sum += bag.total
    return sum

def parse_elf_bags(filename):
    """Parse the elf bags from the file"""
    bags = []
    bag = ElfBag()

    with open(filename, "r") as f:
        # add integer values to a list
        for line in f:
            line = line.strip()
            if line == "":
                bags.append(bag)
                bag = ElfBag()
            else: 
                line = int(line)
                bag.add(line)
    return bags

if __name__ == "__main__":
    # Read input
    with open("input.txt", "r") as f:
        input = f.read()

    # Parse input
