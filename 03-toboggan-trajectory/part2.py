from functools import reduce

with open("input.txt", "r") as f:
    terrain = f.read().splitlines()

pattern_length = len(terrain[0])


def check_slope(slope):
    trees_encountered = 0
    i = 0
    j = 0
    while i <= len(terrain):
        i += slope[1]
        if i >= len(terrain):
            break
        j += slope[0]
        j %= pattern_length
        if terrain[i][j] == "#":
            trees_encountered += 1

    return trees_encountered


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
tree_counts = list(map(check_slope, slopes))
product = reduce((lambda a, b: a * b), tree_counts)

print(product)
