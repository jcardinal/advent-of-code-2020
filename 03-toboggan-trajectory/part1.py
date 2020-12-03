with open("input.txt", "r") as f:
    terrain = f.read().splitlines()

trees_encountered = 0
i = 0
j = 0

while i <= len(terrain):
    i += 1
    if i == len(terrain):
        break
    j += 3
    j %= 31
    if terrain[i][j] == "#":
        trees_encountered += 1

print(trees_encountered)