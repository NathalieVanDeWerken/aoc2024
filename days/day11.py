from lib import load_input


def solve(data, part=1):
    if part == 1:
        return part_one(int(x) for x in data.strip().split(' '))
    elif part == 2:
        return part_two(int(x) for x in data.strip().split(' '))


def part_one(data):
    for _ in range(25):
        new_stones = []
        for stone in data:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                st = str(stone)
                new_stones.append(int(st[:len(st)//2]))
                new_stones.append(int(st[len(st)//2:]))
            else:
                new_stones.append(2024 * stone)
        data = new_stones
    return len(data)


def part_two(data):
    stones = dict()
    for stone in data:
        if stone not in stones:
            stones[stone] = 0
        stones[stone] += 1
    for _ in range(75):
        new_stones = dict()
        for stone, num in stones.items():
            if stone == 0:
                if 1 not in new_stones:
                    new_stones[1] = 0
                new_stones[1] += num
            elif len(str(stone)) % 2 == 0:
                st = str(stone)
                if int(st[:len(st) // 2]) not in new_stones:
                    new_stones[int(st[:len(st) // 2])] = 0
                new_stones[int(st[:len(st) // 2])] += num
                if int(st[len(st) // 2:]) not in new_stones:
                    new_stones[int(st[len(st) // 2:])] = 0
                new_stones[int(st[len(st) // 2:])] += num
            else:
                if 2024 * stone not in new_stones:
                    new_stones[2024 * stone] = 0
                new_stones[2024 * stone] += num
        stones = new_stones
    return sum(stones.values())


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
