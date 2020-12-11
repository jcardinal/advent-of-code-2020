import copy


def total_occupied_seats(seat_array):
    total = 0
    for i in range(len(seat_array)):
        for j in range(len(seat_array[i])):
            if seat_array[i][j] == "#":
                total += 1
    return total


def occupancy(i, j, seat_array):
    # Check if seat location is out of bounds
    if i not in range(len(seat_array)) or j not in range(len(seat_array[i])):
        return 0

    if seat_array[i][j] == "#":
        return 1
    else:
        return 0


def count_neighbors(i, j, seat_array):
    return (
        occupancy(i - 1, j - 1, seat_array)
        + occupancy(i - 1, j, seat_array)
        + occupancy(i - 1, j + 1, seat_array)
        + occupancy(i, j - 1, seat_array)
        + occupancy(i, j + 1, seat_array)
        + occupancy(i + 1, j - 1, seat_array)
        + occupancy(i + 1, j, seat_array)
        + occupancy(i + 1, j + 1, seat_array)
    )


with open("input.txt", "r") as f:
    seat_data = f.read().splitlines()

seat_array = []
for i in range(len(seat_data)):
    row = []
    for j in range(len(seat_data[i])):
        row.append(seat_data[i][j])
    seat_array.append(row)

loops = 0
updated_seat_array = []
while updated_seat_array != seat_array:
    if loops > 0:
        seat_array = copy.deepcopy(updated_seat_array)
    updated_seat_array = copy.deepcopy(seat_array)
    for i in range(len(seat_array)):
        for j in range(len(seat_array[i])):
            if seat_array[i][j] == "L":
                num_neighbors = count_neighbors(i, j, seat_array)
                if num_neighbors == 0:
                    updated_seat_array[i][j] = "#"
            elif seat_array[i][j] == "#":
                num_neighbors = count_neighbors(i, j, seat_array)
                if num_neighbors >= 4:
                    updated_seat_array[i][j] = "L"
    loops += 1


print(total_occupied_seats(seat_array))
