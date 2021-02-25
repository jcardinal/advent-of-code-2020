with open("input.txt", "r") as f:
    entries = f.read().splitlines()

northsouth = 0
eastwest = 0
directions = "NESW"
facing = directions[1]

for entry in entries:
    if entry[0] == "N":
        northsouth += int(entry[1:])
    elif entry[0] == "S":
        northsouth -= int(entry[1:])
    elif entry[0] == "E":
        eastwest += int(entry[1:])
    elif entry[0] == "W":
        eastwest -= int(entry[1:])
    elif entry[0] == "L":
        facing = directions[int(directions.index(facing) - int(entry[1:]) / 90) % 4]
    elif entry[0] == "R":
        facing = directions[int(directions.index(facing) + int(entry[1:]) / 90) % 4]
    elif entry[0] == "F":
        if facing == "N":
            northsouth += int(entry[1:])
        elif facing == "S":
            northsouth -= int(entry[1:])
        elif facing == "E":
            eastwest += int(entry[1:])
        elif facing == "W":
            eastwest -= int(entry[1:])

print(abs(northsouth) + abs(eastwest))