# This was my initial solution to part 1. It's pretty naive and actually
# much slower than part 2, which can solve both parts.


def iter_pairs(val: str):
    for i, tens_dig in enumerate(val):
        for ones_dig in val[i + 1 :]:
            yield (int(tens_dig + ones_dig))


def solve():
    with open("input.txt") as f:
        lines = [line.strip() for line in f]

    total = 0
    for line in lines:
        largest = 0
        for pair in iter_pairs(line):
            if pair > largest:
                largest = pair

        total += largest

    print(total)


if __name__ == "__main__":
    solve()
