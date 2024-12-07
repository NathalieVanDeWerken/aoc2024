from lib import load_input


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    answer = 0
    for line in data:
        result = int(line.split(': ')[0])
        digits = [int(x) for x in line.split(': ')[1].split(' ')]
        if can_make_it(0, digits, result):
            answer += result
    return answer


def can_make_it(result, digits, final):
    if len(digits) == 0:
        return result == final
    return can_make_it(result + digits[0], digits[1:], final) or can_make_it(result * digits[0], digits[1:], final)


def part_two(data):
    answer = 0
    for line in data:
        result = int(line.split(': ')[0])
        digits = [int(x) for x in line.split(': ')[1].split(' ')]
        if can_make_it2(0, digits, result):
            answer += result
    return answer


def can_make_it2(result, digits, final):
    if len(digits) == 0:
        return result == final
    return (can_make_it2(result + digits[0], digits[1:], final) or can_make_it2(result * digits[0], digits[1:], final)
            or can_make_it2(int(str(result) + str(digits[0])), digits[1:], final))


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
