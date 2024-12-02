from copy import copy

from lib import load_input
from parser import read_input_list_of_lists


def solve(data, part=1):
    lines = read_input_list_of_lists(data)
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    count = 0
    for line in data:
        differences = [line[i + 1] - line[i] for i in range(0, len(line) - 1)]
        count += all(map(lambda x: 1 <= x <= 3, differences)) or all(map(lambda x: -3 <= x <= -1, differences))
    return count


def part_two(data):
    count = 0
    for line in data:
        add = False
        for x in range(len(line)):
            line2 = copy(line)
            line2.pop(x)
            differences = [line2[i + 1] - line2[i] for i in range(0, len(line2) - 1)]
            add = all(map(lambda x: 1 <= x <= 3, differences)) or all(map(lambda x: -3 <= x <= -1, differences)) or add
        if add:
            count += 1
    return count


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
