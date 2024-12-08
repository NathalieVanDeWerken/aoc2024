from lib import load_input


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    antennas = dict()
    result = set()
    for x, line in enumerate(data):
        for y, pos in enumerate(line):
            if pos != '.':
                if pos not in antennas.keys():
                    antennas[pos] = list()
                antennas[pos].append((x, y))
    for item in antennas.values():
        for an1 in item:
            for an2 in item:
                if an1 == an2:
                    continue
                dx = an1[0] - an2[0]
                dy = an1[1] - an2[1]

                if 0 <= an1[0] + dx < len(data) and 0 <= an1[1] + dy < len(data[0]):
                    result.add((an1[0] + dx, an1[1] + dy))
                if 0 <= an2[0] - dx < len(data[0]) and 0 <= an2[1] - dy < len(data[0]):
                    result.add((an2[0] - dx, an2[1] - dy))
    return len(result)


def part_two(data):
    antennas = dict()
    result = set()
    for x, line in enumerate(data):
        for y, pos in enumerate(line):
            if pos != '.':
                if pos not in antennas.keys():
                    antennas[pos] = list()
                antennas[pos].append((x, y))
    for item in antennas.values():
        for an1 in item:
            for an2 in item:
                if an1 == an2:
                    continue
                dx = an1[0] - an2[0]
                dy = an1[1] - an2[1]
                i = 0
                j = 0
                while 0 <= an1[0] + j * dx < len(data) and 0 <= an1[1] + j * dy < len(data[0]):
                    result.add((an1[0] + j * dx, an1[1] + j * dy))
                    j += 1
                while 0 <= an2[0] - i * dx < len(data[0]) and 0 <= an2[1] - i * dy < len(data[0]):
                    result.add((an2[0] - i * dx, an2[1] - i * dy))
                    i += 1
    return len(result)


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
