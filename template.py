from lib import load_input


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    pass


def part_two(data):
    pass


if __name__ == "__main__":
    print(solve(load_input("small")))
    # print(solve(load_input()))
    # print(solve(load_input("small"), 2))
    # print(solve(load_input(), 2))
