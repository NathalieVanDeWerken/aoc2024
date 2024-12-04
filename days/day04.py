from lib import load_input


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    x, y = len(data[0]), len(data)
    sequences = data.copy()
    columns = []
    for i in range(x):
        column = []
        for j in range(y):
            column.append(data[j][i])
        columns.append(''.join(column))
    sequences = sequences + columns
    for i in range(x):
        diag1, diag2, diag3, diag4 = [], [], [], []
        for j in range(0, min(i, y) + 1):
            diag1.append(data[i-j][j])
            if i != x - 1:
                diag3.append(data[i-j][y-j-1])
        for j in range(0, min(x - i, y)):
            diag2.append(data[i+j][j])
            if i != 0:
                diag4.append(data[i+j][y-j-1])
        sequences = sequences + [''.join(diag1), ''.join(diag2), ''.join(diag3), ''.join(diag4)]
    sequences = sequences + [x[::-1] for x in sequences]
    return sum([x.count('XMAS') for x in sequences])



def part_two(data):
    result = 0
    x = len(data)
    for i in range(x):
        for j in range(x):
            if data[i][j] == 'A' and 0 < i < x - 1 and 0 < j < x - 1:
                result += {data[i-1][j+1], data[i+1][j-1]} == {'M', 'S'} and {data[i-1][j-1], data[i+1][j+1]} == {'M', 'S'}
    return result



if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
