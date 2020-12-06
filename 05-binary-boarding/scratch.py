print(70 * 8 + 4)
print(70 * 8 + 5)
print(71 * 8 + 0)

seat_map = []

for i in range(0, 128):
    seat_map.append((i, []))


seat_map[0][1].append(3)
seat_map[0][1].append(5)
seat_map[0][1].append(1)
seat_map[5][1].append(0)
seat_map[5][1].append(3)

for i in range(0, 7):
    print(len(seat_map[i][1]))

print(len(seat_map[5][1]))

# string = "my_string"
# for i in range(len(string)):
#     print(string[i])
