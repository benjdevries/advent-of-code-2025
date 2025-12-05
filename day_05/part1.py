def solve():
    ranges = []

    with open("input.txt") as f:
        while line := next(f).strip():
            start, stop = line.split("-")
            ranges.append(range(int(start), int(stop) + 1))

        next(f)  # throw away blank line
        ingredients = [int(i.strip()) for i in f]

    fresh_count = 0
    for ingredient in ingredients:
        for r in ranges:
            if ingredient in r:
                fresh_count += 1
                break

    print(fresh_count)


if __name__ == "__main__":
    solve()
