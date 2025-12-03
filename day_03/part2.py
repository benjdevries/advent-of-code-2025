def solve(num_batteries: int, battery_banks):
    total = 0
    for bank in battery_banks:
        battery_idx = 0
        batteries = []
        remaining_batteries = bank
        for i in range(num_batteries, 0, -1):
            # Find the largest available battery, keeping in mind the
            # previous one and the number remaining so we don't run out
            # of choices. By picking the highest available battery for
            # each place value, we are guaranteed to find the highest total.
            cutoff = len(remaining_batteries) + 1 - i
            eligible_next = remaining_batteries[:cutoff]
            battery = max(eligible_next)
            batteries.append(battery)
            battery_idx = remaining_batteries.index(battery)
            # Next battery must be selected only from batteries after the selected one
            remaining_batteries = remaining_batteries[battery_idx + 1 :]

        total += int("".join(batteries))

    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        battery_banks = [line.strip() for line in f]

    print(f"Part 1: {solve(2, battery_banks)}")
    print(f"Part 2: {solve(12, battery_banks)}")
