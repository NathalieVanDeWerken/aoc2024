from lib import load_input
import re

from parser import read_input_singular_line


def solve(data, part=1):
    lines = read_input_singular_line(data)
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines + '\n')


def part_one(data):
    return sum(int(x[0])*int(x[1]) for x in re.findall(r'mul\((\d+),(\d+)\)', data))


def part_two(data):
    return part_one(re.sub(r'don\'t\(\).*?do\(\)|don\'t\(\).*?\n', '', data))


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small_2"), 2))
    print(solve(load_input(), 2))
