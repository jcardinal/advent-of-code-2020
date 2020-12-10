# Simplify toggling between example data and main input
example = False
if example == True:
    preamble_length = 5
    filename = "example.txt"
else:
    preamble_length = 25
    filename = "input.txt"

# Do the work
with open(filename, "r") as f:
    xmas_data = list(map(int, f.readlines()))

for i in range(preamble_length, len(xmas_data)):
    success_count = 0
    for j in range(i - 1, i - preamble_length, -1):
        if xmas_data[i] - xmas_data[j] in xmas_data[i - preamble_length : j]:
            success_count += 1

    if success_count == 0:
        print("Invalid number is", xmas_data[i])
