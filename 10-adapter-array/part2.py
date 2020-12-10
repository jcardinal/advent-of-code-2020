from collections import Counter

with open("input.txt", "r") as f:
    adapters = list(map(int, f.readlines()))

adapters.sort()
adapters.insert(0, 0)
adapters.append(max(adapters) + 3)
counter = Counter({0: 1})

for adapter in adapters:
    counter[adapter + 1] += counter[adapter]
    counter[adapter + 2] += counter[adapter]
    counter[adapter + 3] += counter[adapter]

print(counter[max(adapters)])
