import itertools
import math

factor_cache: dict[int, set[int]] = {}


def factors(num: int) -> set[int]:
    if num in factor_cache:
        return factor_cache[num]

    res: set[int] = set()
    for i in range(1, int(math.sqrt(num) + 1)):
        if num % i == 0:
            res.add(i)
            res.add(num // i)

    factor_cache[num] = res
    return res


def solve():
    with open("input.txt") as f:
        txt = f.read()

    acc = 0

    ranges = txt.split(",")
    for r in ranges:
        start, end = r.split("-")
        start, end = int(start), int(end)
        for x in range(start, end + 1):
            val = str(x)

            chunk_sizes = factors(len(val))

            for size in chunk_sizes:
                if size == len(val):
                    continue

                chunks = set(itertools.batched(val, size))
                if len(chunks) == 1:
                    acc += x
                    break

    print(acc)


if __name__ == "__main__":
    solve()
