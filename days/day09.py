from lib import load_input


def solve(data, part=1):
    if part == 1:
        return part_one([int(x) for x in data.strip()])
    elif part == 2:
        return part_two([int(x) for x in data.strip()])


def part_one(data):
    result = 0
    ind = 0
    j = len(data) - 1
    for i, char in enumerate(data):
        if i % 2 == 0:
            for _ in range(char):
                result += ind * i // 2
                ind += 1
        else:
            for _ in range(char):
                while j % 2 == 1 or data[j] == 0:
                    j -= 1
                if j <= i:
                    break
                result += j // 2 * ind
                data[j] -= 1
                ind += 1
    return result


def part_two(data):
    result = 0
    ind = 0
    moved = [False for _ in range(len(data))]
    for i, char in enumerate(data):
        if moved[i]:
            ind += data[i]
        elif i % 2 == 0:
            for _ in range(char):
                result += int(ind * i / 2)
                ind += 1
        else:
            j = len(data) - 1
            while char > 0 and j > i:
                while j % 2 == 1 or data[j] > char or moved[j]:
                    j -= 1
                if j <= i:
                    break
                for _ in range(data[j]):
                    result += j // 2 * ind
                    ind += 1
                char -= data[j]
                moved[j] = True
            ind += char
    return result


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
