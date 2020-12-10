with open("input.txt", "r") as f:
    adapters = list(map(int, f.readlines()))

adapters.sort()

cur_joltage = 0
dist_joltage_diffs = {1: 0, 2: 0, 3: 0}
for adapter in adapters:
    dist_joltage_diffs[adapter - cur_joltage] += 1
    cur_joltage = adapter

# Add diff between final adapter and device's built-in adapter
dist_joltage_diffs[3] += 1

print(dist_joltage_diffs[1] * dist_joltage_diffs[3])