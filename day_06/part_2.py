import functools
import operator

OPERATORS = {"+": operator.add, "*": operator.mul}


def operand_groups(columns):
    group = []
    for column in columns:
        val = "".join(column).strip()
        if val:
            group.append(int(val))
        else:
            yield group
            group = []
    yield group


def solve():
    with open("input.txt") as f:
        rows = [r.rstrip("\n") for r in f.readlines()]
        ops = rows.pop()

    columns = list(zip(*rows))[::-1]
    problems = list(operand_groups(columns))

    operators = [op.strip() for op in ops[::-1] if op.strip()]

    total = 0

    for operands, op in zip(problems, operators):
        result = functools.reduce(OPERATORS[op], operands)
        total += result

    print(total)


if __name__ == "__main__":
    solve()
