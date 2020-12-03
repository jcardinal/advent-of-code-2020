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

product = 1
for slope in slopes:
    trees_encountered = check_slope(slope)
    product *= trees_encountered

print(product)