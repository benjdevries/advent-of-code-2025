import functools
import operator

OPERATORS = {"+": operator.add, "*": operator.mul}


def solve():
    with open("input.txt") as f:
        rows = [r.strip().split() for r in f.readlines()]
        ops = rows.pop()

    total = 0

    for *operands, op in zip(*rows, ops):
        result = functools.reduce(OPERATORS[op], [int(x) for x in operands])
        total += result

    print(total)


if __name__ == "__main__":
    solve()
