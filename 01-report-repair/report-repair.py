with open('input.txt', 'r') as f:
    entries = f.read().splitlines()

for i in range(len(entries)):
    entries[i] = int(entries[i])

a, b = 0, 0

for i in range(len(entries)):
    if a != 0 or b != 0:
        break
    for j in range(len(entries) - i):
        if entries[i] + entries[i+j] == 2020:
            a = i
            b = i+j
            break

print(f"The two numbers are {entries[a]} and {entries[b]}")
print(f"The product is {entries[a]*entries[b]}")
