from lib import load_input


def solve(data, part=1):
    if part == 1:
        return part_one([[int(x) for x in y] for y in data.splitlines()])
    elif part == 2:
        return part_two([[int(x) for x in y] for y in data.splitlines()])


def part_one(data):
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = 0
    for x1 in range(len(data)):
        for y1 in range(len(data[x1])):
            if data[x1][y1] == 0:
                res = set()
                to_visit = [(x1, y1)]
                while len(to_visit) > 0:
                    x, y = to_visit.pop(0)
                    if data[x][y] == 9:
                        res.add((x, y))
                        continue
                    for dx, dy in dir:
                        if 0 <= x + dx < len(data) and 0 <= y + dy < len(data[0]):
                            if data[x + dx][y + dy] == data[x][y] + 1:
                                to_visit.append((x + dx, y + dy))
                result += len(res)
    return result



def part_two(data):
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = 0
    for x1 in range(len(data)):
        for y1 in range(len(data[x1])):
            if data[x1][y1] == 0:
                res = list()
                to_visit = [(x1, y1)]
                while len(to_visit) > 0:
                    x, y = to_visit.pop(0)
                    if data[x][y] == 9:
                        res.append((x, y))
                        continue
                    for dx, dy in dir:
                        if 0 <= x + dx < len(data) and 0 <= y + dy < len(data[0]):
                            if data[x + dx][y + dy] == data[x][y] + 1:
                                to_visit.append((x + dx, y + dy))
                result += len(res)
    return result


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
