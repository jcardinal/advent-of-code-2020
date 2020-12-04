import re

with open("valid.txt", "r") as f:
    passport_list = f.read().split("\n\n")

num_required_fields = 8

# Convert list of strings to list of dictionaries
i = 0
for passport in passport_list:
    passport = " ".join(passport.splitlines())
    passport = dict(kv.split(":") for kv in passport.split(" "))
    passport_list[i] = passport
    i += 1


def validate_passport(passport):
    valid_byr_range = range(1920, 2002 + 1)
    valid_iyr_range = range(2010, 2020 + 1)
    valid_eyr_range = range(2020, 2030 + 1)
    valid_hgt_regex = "^[0-9]{1,3}(in|cm)$"
    valid_cm_hgt_range = range(150, 193 + 1)
    valid_in_hgt_range = range(59, 76 + 1)
    valid_hcl_regex = "^#[a-f0-9]{6}$"
    valid_ecls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    valid_pid_regex = "^[0-9]{9}$"

    # Check for required fields
    if len(passport) == num_required_fields:
        pass
    elif len(passport) == num_required_fields - 1:
        if not "cid" in passport:
            pass
        else:
            return False
    else:
        return False

    # Validate fields
    if int(passport["byr"]) not in valid_byr_range:
        return False

    if int(passport["iyr"]) not in valid_iyr_range:
        return False

    if int(passport["eyr"]) not in valid_eyr_range:
        return False

    if re.match(valid_hgt_regex, passport["hgt"]):
        if passport["hgt"][-2:] == "cm":
            if int(passport["hgt"][0:-2]) in valid_cm_hgt_range:
                pass
        elif int(passport["hgt"][0:-2]) in valid_in_hgt_range:
            pass
        else:
            return False
    else:
        return False

    if not re.match(valid_hcl_regex, passport["hcl"]):
        return False

    if passport["ecl"] not in valid_ecls:
        return False

    if not re.match(valid_pid_regex, passport["pid"]):
        return False

    return True


# Count valid passports
num_valid_passports = 0
for passport in passport_list:
    if validate_passport(passport):
        num_valid_passports += 1

print(num_valid_passports)
