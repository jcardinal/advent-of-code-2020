import re


def validate_boarding_pass(boarding_pass):
    valid_boarding_pass_re = "^[BF]{7}[LR]{3}$"
    return re.match(valid_boarding_pass_re, boarding_pass)


def get_seat_id(boarding_pass):
    boarding_pass = boarding_pass.replace("F", "0").replace("B", "1")
    boarding_pass = boarding_pass.replace("L", "0").replace("R", "1")
    row = int(boarding_pass[0:7], base=2)
    col = int(boarding_pass[7:], base=2)
    seat_id = row * 8 + col
    return seat_id


def get_missing_seat_id(boarding_passes):
    seat_map = []
    for i in range(0, 128):
        seat_map.append((i, []))

    for i in range(len(boarding_passes)):
        boarding_passes[i] = boarding_passes[i].replace("F", "0").replace("B", "1")
        boarding_passes[i] = boarding_passes[i].replace("L", "0").replace("R", "1")
        row = int(boarding_passes[i][0:7], base=2)
        col = int(boarding_passes[i][7:], base=2)
        seat_map[row][1].append(col)

    for i in range(0, 128):
        if len(seat_map[i][1]) == 7:
            my_row = i
            break

    for i in range(0, 6):
        if i not in seat_map[my_row][1]:
            my_col = i

    return my_row * 8 + my_col


with open("input.txt", "r") as f:
    boarding_passes = f.read().splitlines()

my_seat_id = get_missing_seat_id(boarding_passes)
print(my_seat_id)
