with open("input.txt", "r") as f:
    entries = f.read().splitlines()

for i in range(len(entries)):
    entries[i] = int(entries[i])

a, b, c = 0, 0, 0

for i in range(len(entries)):
    if a != 0 or b != 0 or c != 0:
        break
    for j in range(len(entries) - i):
        if a != 0 or b != 0 or c != 0:
            break
        for k in range(len(entries) - (i + j)):
            if entries[i] + entries[i + j] + entries[i + j + k] == 2020:
                a = i
                b = i + j
                c = i + j + k
                break

print(f"The three numbers are {entries[a]}, {entries[b]}, and {entries[c]}")
print(f"The product is {entries[a]*entries[b]*entries[c]}")
