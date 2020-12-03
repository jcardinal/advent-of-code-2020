with open("input.txt", "r") as f:
    password_list = f.read().splitlines()

valid_password_count = 0

for item in password_list:
    min = int(item[: int(item.index("-"))])
    max = int(item[int(item.index("-")) + 1 : item.index(" ")])
    test_char = item[int(item.index(":") - 1)]
    test_pass = item[int(item.index(":") + 2) :]
    char_count = 0

    for char in test_pass:
        if char == test_char:
            char_count += 1

    if char_count >= min and char_count <= max:
        valid_password_count += 1


print(valid_password_count)