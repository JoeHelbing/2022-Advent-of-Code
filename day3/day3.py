PRIORITY_VALUES = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


def parse_input(input_file):
    with open(input_file) as f:
        return [line.strip() for line in f]


class ElfGroup:
    def __init__(self, Rucksacks):
        self.Rucksack1 = Rucksacks[0]._compartments[0] + Rucksacks[0]._compartments[1]
        self.Rucksack2 = Rucksacks[1]._compartments[0] + Rucksacks[1]._compartments[1]
        self.Rucksack3 = Rucksacks[2]._compartments[0] + Rucksacks[2]._compartments[1]
        self._priority_value = None

    def duplicated(self):
        whole_bag = set(self.Rucksack1) & set(self.Rucksack2) & set(self.Rucksack3)
        duplicate = next(iter(whole_bag))
        self._priority_value = PRIORITY_VALUES.index(duplicate) + 1
        return self._priority_value


class Rucksack:
    def __init__(self, items):
        length = len(items)
        split_index = length // 2
        self._compartments = (items[:split_index], items[split_index:])
        self._priority_value = None

    def duplicated_items(self):
        duplicate = set(self._compartments[0]) & set(self._compartments[1])
        duplicate = next(iter(duplicate))
        self._priority_value = PRIORITY_VALUES.index(duplicate) + 1
        return None

    def priority_value(self):
        return self._priority_value


def main():
    items = parse_input("day3.txt")
    sum1 = 0
    sum2 = 0
    rucksacks = []
    for i, item in enumerate(items):
        rucksack = Rucksack(item)
        rucksack.duplicated_items()
        sum1 += rucksack.priority_value()
        rucksacks.append(rucksack)
        if (i + 1) % 3 == 0:
            elf_group = ElfGroup(rucksacks)
            rucksacks = []
            sum2 += elf_group.duplicated()
    print(f"Part 1 Sum: {sum1}")
    print(f"Part 2 Sum: {sum2}")


if __name__ == "__main__":
    main()
