from lib import load_input


def solve(data, part=1):
    list1, list2 = [], []
    for x in data.splitlines():
        x = x.split()
        list1.append(int(x[0]))
        list2.append(int(x[1]))
    if part == 1:
        return part_one(list1, list2 )
    elif part == 2:
        return part_two(list1, list2)


def part_one(list1, list2):
    return sum(abs(x[0] - x[1]) for x in zip(sorted(list1), sorted(list2)))


def part_two(list1, list2):
    return sum(x * list2.count(x) for x in list1)


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
