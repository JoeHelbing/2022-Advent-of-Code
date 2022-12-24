def parse_input():
    with open("input.txt") as f:
        input = f.readline()
        input = input.strip()
        return input


def part1(input):
    # loops through each character in input
    four = []

    for i, letter in enumerate(input):
        if i < 3:
            four.append(letter)
            continue
        four.append(letter)
        if len(set(four)) == 4:
            return i + 1
        four.pop(0)


def part2(input):
    # loops through each character in input
    fourteen = []

    for i, letter in enumerate(input):
        if i < 13:
            fourteen.append(letter)
            continue

        fourteen.append(letter)
        if len(set(fourteen)) == 14:
            return i + 1
        fourteen.pop(0)

if __name__ == "__main__":
    input = parse_input()
    print(f"Marker at {part1(input)}")
    print(f"Marker at {part2(input)}")
