import copy

from lib import load_input


def solve(data, part=1):
    if part == 1:
        return part_one(data)
    elif part == 2:
        return part_two(data)


def part_one(data):
    grid = list()
    x, y = 0, 0
    dir = 0
    for line in data.splitlines():
        grid.append([x for x in line])
        if '^' in line:
            y = line.index('^')
            x = grid.index([x for x in line])
    grid[x][y] = '.'
    visited = {(x, y)}
    while -1 < x < len(grid) and -1 < y < len(grid[0]):
        visited.add((x, y))
        x, y, dir = make_move(grid, x, y, dir)
    return len(visited)


def make_move(grid, x, y, dir):
    if dir == 0:
        if x == 0:
            return x - 1, y, dir
        elif grid[x - 1][y] == '#':
            return make_move(grid, x, y, 1)
        return x - 1, y, dir
    elif dir == 1:
        if y == len(grid[0]) - 1:
            return x, y + 1, dir
        elif grid[x][y + 1] == '#':
            return make_move(grid, x, y, 2)
        return x, y + 1, dir
    elif dir == 2:
        if x == len(grid[0]) - 1:
            return x + 1, y, dir
        elif grid[x + 1][y] == '#':
            return make_move(grid, x, y, 3)
        return x + 1, y, dir
    else:
        if y == 0:
            return x, y - 1, dir
        elif grid[x][y - 1] == '#':
            return make_move(grid, x, y, 0)
        return x, y - 1, dir


def part_two(data):
    grid = list()
    x, y = 0, 0
    dir = 0
    for line in data.splitlines():
        grid.append([x for x in line])
        if '^' in line:
            y = line.index('^')
            x = grid.index([x for x in line])
    grid[x][y] = '.'
    x_start, y_start = x, y
    result = 0
    for x in range(0, len(grid)):
        print(x/len(grid) *100)
        for y in range(0, len(grid[0])):
            grid2 = copy.deepcopy(grid)
            grid2[x][y] = '#'
            if leads_to_cycle(x_start, y_start, 0, grid2):
                result += 1
    return result


def leads_to_cycle(x, y, dir, grid):
    visited = {(x, y, dir)}
    while -1 < x < len(grid) and -1 < y < len(grid[0]):
        x, y, dir = make_move(grid, x, y, dir)
        if (x, y, dir) in visited: return True
        visited.add((x, y, dir))
    return False


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
