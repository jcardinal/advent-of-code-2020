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


with open("input.txt", "r") as f:
    boarding_passes = f.read().splitlines()

highest_seat_id = 0

for boarding_pass in boarding_passes:
    if not validate_boarding_pass(boarding_pass):
        raise Exception(f"Invalid boarding pass found: {boarding_pass}")
    seat_id = get_seat_id(boarding_pass)
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id

print(highest_seat_id)
