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

            if len(val) % 2 != 0:
                continue

            split_idx = len(val) // 2
            if val[:split_idx] == val[split_idx:]:
                acc += x

    print(acc)


if __name__ == "__main__":
    solve()
