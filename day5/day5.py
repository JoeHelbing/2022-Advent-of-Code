class Stack:
    def __init__(self, stack=[]):
        self.items = stack

    def crane_drop(self, item):
        # item can be a list or a single item
        if type(item) == list:
            self.items.extend(item)
        else:
            self.items.append(item)

    def crane_lift(self):
        return self.items.pop()

    def crane_multi_lift(self, how_many_boxes):
        # creates a list of how_many_boxes items and returns it
        picked_up = []

        for _ in range(how_many_boxes):
            crate = self.crane_lift()
            picked_up.append(crate)

        picked_up = picked_up[::-1]

        return picked_up

    def peek(self):
        return self.items[-1]

    def get_stack(self):
        return self.items


class Storage:
    def __init__(self, stacks, crane='CrateMover 9001'):
        self.stacks = stacks
        self.crane = crane
        for i, stack in enumerate(self.stacks):
            self.stacks[i] = Stack(stack)
            

    def top_stack(self):
        # returns name of top box for each stack
        return ''.join([stack.peek() for stack in self.stacks])

    def move(self, how_many_boxes, from_stack, to_stack):
        # change from_stack and to_stack to index
        from_stack -= 1
        to_stack -= 1
        # check which move to do
        if self.crane == "CrateMover 9001":
            self._multi_move(how_many_boxes, from_stack, to_stack)
        elif self.crane == "CrateMover 9000":
            self._single_move(how_many_boxes, from_stack, to_stack)


    def _single_move(self, how_many_boxes, from_stack, to_stack):
        # moves how_many_boxes from from_stack to to_stack
        for _ in range(how_many_boxes):
            self.stacks[to_stack].crane_drop(self.stacks[from_stack].crane_lift())
    
    def _multi_move(self, how_many_boxes, from_stack, to_stack):
        # moves how_many_boxes from from_stack to to_stack
        self.stacks[to_stack].crane_drop(self.stacks[from_stack].crane_multi_lift(how_many_boxes))


def parse_input():
    # returns list of stacks
    with open("input.txt") as f:
        stacks = [[], [], [], [], [], [], [], [], []]
        moves = []
        trigger = False
        for line in f:
            # finds the trigger point of \n line
            if line == "\n":
                trigger = True
                for stack in stacks:
                    stack.reverse()
                continue
            # if trigger is false, it means we are still reading the stacks
            if not trigger:
                # if line does not contain '[', it means it is an empty line and thats 
                # the line of stack numbers
                if "[" not in line:
                    continue
                line = [line[i : i + 4] for i in range(0, len(line), 4)]
                for i, box in enumerate(line):
                    box = (
                        box.replace("[", "")
                        .replace("]", "")
                        .replace("\n", "")
                        .replace(" ", "")
                    )
                    if box == "":
                        continue
                    stacks[i].append(box)
            # if trigger is true, it means we are reading the moves
            else:
                line = line.split()
                moves.append(tuple((int(line[1]), int(line[3]), int(line[5]))))
        return stacks, moves


def run_simulation(stacks, moves, crane):
    storage = Storage(stacks, crane=crane)
    for move in moves:
        storage.move(move[0], move[1], move[2])
    return storage


if __name__ == "__main__":
    stacks, moves = parse_input()
    storage = run_simulation(stacks, moves, crane="CrateMover 9000")
    print(f"Top boxes CrateMover 9000: {storage.top_stack()}")
    stacks, moves = parse_input()
    storage = run_simulation(stacks, moves, crane="CrateMover 9001")
    print(f"Top boxes CrateMover 9001: {storage.top_stack()}")