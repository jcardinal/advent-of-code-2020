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
    num_neighbors = occupancy(i - 1, j - 1, seat_array)
    num_neighbors += occupancy(i - 1, j, seat_array)
    num_neighbors += occupancy(i - 1, j + 1, seat_array)
    num_neighbors += occupancy(i, j - 1, seat_array)
    num_neighbors += occupancy(i, j + 1, seat_array)
    num_neighbors += occupancy(i + 1, j - 1, seat_array)
    num_neighbors += occupancy(i + 1, j, seat_array)
    num_neighbors += occupancy(i + 1, j + 1, seat_array)
    return num_neighbors


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


for i in range(len(seat_array)):
    print(seat_array[i])
print(total_occupied_seats(seat_array))

"""
Things I need to do:
x convert input to a 2-dimensional array (2d list? numpy array? import array module?)
x learn to deep copy that structure (to make a copy, change seats based on rules)
x learn to check equality of this structure (eg; did any seats change or have we stabilized?)


get_adjacent(seat): given a seat, return the locations of all adjacent seats
all_vacant(seats): given a list of seats, return True if all are vacant, or False if any are occupied
count_occupied(seats): given a list of seats, return number that are occupied
count_neighbors(seat, array): given a seat and array of seats, count neighbors (occupied adjacent seats)

given [3][3] (aka: [i][j]), adjacent seats would be:
[2][2], [2][3], [2][4] (above) aka: [i-1][j-1], [i-1][j], [i-1][j+1] 
[3][2], [3][4] (left and right beside) aka: [i][j-1], [i][j+1]
[4][2], [4][3], [4][4] (below) aka: [i+1][j-1], [i+1][j], [i+1][j+1]
UNLESS any of those seats don't exist because we're near an edge

"""