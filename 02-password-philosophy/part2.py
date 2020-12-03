with open('input.txt', 'r') as f:
    password_list = f.read().splitlines()

valid_password_count = 0

for item in password_list:
    pos1 = int(item[:int(item.index('-'))]) - 1
    pos2 = int(item[int(item.index('-')) + 1:item.index(' ')]) - 1
    test_char = item[int(item.index(':') - 1)]
    test_pass = item[int(item.index(':') + 2):]

    if test_pass[pos1] == test_char:
        if test_pass[pos2] != test_char:
            valid_password_count += 1
    elif test_pass[pos2] == test_char:
        valid_password_count += 1


print(valid_password_count)
