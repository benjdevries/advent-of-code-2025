def solve():
    ranges = []

    with open("input.txt") as f:
        while line := next(f).strip():
            start, stop = line.split("-")
            ranges.append((int(start), int(stop)))

    ranges.sort()
    merged_ranges = [ranges[0]]

    for r in ranges:
        mr = merged_ranges.pop()
        if r[0] <= mr[1]:
            mr = (mr[0], max(mr[1], r[1]))
            merged_ranges.append(mr)
        else:
            merged_ranges.extend([mr, r])

    fresh_count = 0

    for mr in merged_ranges:
        fresh_count += mr[1] - mr[0] + 1

    print(fresh_count)


if __name__ == "__main__":
    solve()
