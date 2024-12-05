from lib import load_input


def solve(data, part=1):
    if part == 1:
        return part_one(data)
    elif part == 2:
        return part_two(data)


def part_one(data):
    rules = dict()
    result = 0
    for rule in list(map(lambda x: x.split('|'), data.split('\n\n')[0].split('\n'))):
        if rule[1] not in rules:
            rules[rule[1]] = set()
        rules[rule[1]].add(rule[0])
    orders = list(map(lambda x: x.split(','), data.split('\n\n')[1].split('\n')))
    for order in orders:
        printed = set()
        correct = True
        for el in order:
            if el in rules and len(rules[el].difference(printed).intersection(order)) != 0:
                correct = False
            printed.add(el)
        if correct:
            result += int(order[int(len(order)/2)])
    return result


def part_two(data):
    rules = dict()
    incorrect = list()
    for rule in list(map(lambda x: x.split('|'), data.split('\n\n')[0].split('\n'))):
        if rule[1] not in rules:
            rules[rule[1]] = set()
        rules[rule[1]].add(rule[0])
    orders = list(map(lambda x: x.split(','), data.split('\n\n')[1].split('\n')))
    for order in orders:
        printed = set()
        correct = False
        for el in order:
            if el in rules and len(rules[el].difference(printed).intersection(order)) != 0:
                correct = True
            printed.add(el)
        if correct:
            incorrect.append(order)
    result = 0
    for order in incorrect:
        corrected_order = list()
        for _ in range(len(order)):
            for el in order:
                if el not in rules or len(rules[el].difference(corrected_order).intersection(order)) == 0:
                    corrected_order.append(el)
                    order.remove(el)
                    break
        result += int(corrected_order[int(len(corrected_order)/2)])
    return result


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
