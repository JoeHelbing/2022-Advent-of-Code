

def parse_input():
    """
    parse the input.txt file and returns list of tuples
    """
    with open('input.txt') as f:
        return [tuple(line.strip().split(",")) for line in f]


def expand_assignments(data):
    """
    expands the min and max numbers into a list of numbers
    """
    for elf1, elf2 in data:
        min1, max1 = elf1.split("-")
        min2, max2 = elf2.split("-")
        yield list(range(int(min1), int(max1) + 1)), list(range(int(min2), int(max2) + 1))


def check_roles(data):
    # goes through the data and calls the sub function to check
    for elf1, elf2 in data:
        # choose subset by length (shorter one will always be a subset of the longer one)
        if len(elf1) > len(elf2):
            yield fully_encompass(elf1, elf2)
        else:
            yield fully_encompass(elf2, elf1)


def fully_encompass(elf1, elf2):
    # does the actual check
    elf1 = set(elf1)
    elf2 = set(elf2)
    if elf1.issuperset(elf2):
        return True
    else:
        return False
    


def has_overlap(data):
    # does the actual check

    for elf1, elf2 in data:
        elf1 = set(elf1)
        elf2 = set(elf2)
        if elf1.intersection(elf2):
            yield True
        else:
            yield False


if __name__ == '__main__':
    # part 1
    data = parse_input()
    data = list(expand_assignments(data))
    print(f"Fully Encompassed Pairs: {sum(list(check_roles(data)))}")
    # part 2
    print(f"Overlapping Pairs: {sum(list(has_overlap(data)))}")

    