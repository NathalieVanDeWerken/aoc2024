from lib import load_input


def solve(data, part=1):
    if part == 1:
        return part_one(data.splitlines())
    elif part == 2:
        return part_two(data.splitlines())


def part_one(data):
    done = set()
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    res = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            area = 1
            per = 0
            if (x, y) in done:
                continue
            to_visit = [(x, y)]
            while len(to_visit) > 0:
                x1, y1 = to_visit.pop(0)
                done.add((x1, y1))
                for dx, dy in dirs:
                    if 0 <= x1 + dx < len(data) and 0 <= y1 + dy < len(data[x1]):
                        if data[x1 + dx][y1 + dy] == data[x][y]:
                            if (x1 + dx, y1 + dy) not in done:
                                area += 1
                                to_visit.append((x1 + dx, y1 + dy))
                                done.add((x1 + dx, y1 + dy))
                        else:
                            per += 1
                    else:
                        per += 1
            res += per * area
    return res


def part_two(data):
    done = set()
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    res = 0
    count = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            area = 1
            per = 0
            per_until = list()
            if (x, y) in done:
                continue
            to_visit = [(x, y)]
            while len(to_visit) > 0:
                x1, y1 = to_visit.pop(0)
                done.add((x1, y1))
                for dx, dy in dirs:
                    if 0 <= x1 + dx < len(data) and 0 <= y1 + dy < len(data[x1]):
                        if data[x1 + dx][y1 + dy] == data[x][y]:
                            if (x1 + dx, y1 + dy) not in done:
                                area += 1
                                to_visit.append((x1 + dx, y1 + dy))
                                done.add((x1 + dx, y1 + dy))
                        else:
                            if dx == 0 and not((x1 + 1, y1 + dy, dx, dy) in per_until or (x1 - 1, y1 + dy, dx, dy) in per_until):
                                per += 1
                            if dy == 0 and not((x1 + dx, y1 + 1, dx, dy) in per_until or (x1 + dx, y1 - 1, dx, dy) in per_until):
                                per += 1
                            per_until.append((x1 + dx, y1 + dy, dx, dy))
                    else:
                        if dx == 0 and not ((x1 + 1, y1 + dy, dx, dy) in per_until or (x1 - 1, y1 + dy, dx, dy) in per_until):
                            per += 1
                        if dy == 0 and not ((x1 + dx, y1 + 1, dx, dy) in per_until or (x1 + dx, y1 - 1, dx, dy) in per_until):
                            per += 1
                        per_until.append((x1 + dx, y1 + dy, dx, dy))
            if per % 2 == 1:
                per -= 1
            res += per * area
    return res

if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
