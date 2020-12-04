with open("input.txt", "r") as f:
    passport_list = f.read().split("\n\n")

# Convert list of strings to list of dictionaries
i = 0
for passport in passport_list:
    passport = " ".join(passport.splitlines())
    passport = dict(kv.split(":") for kv in passport.split(" "))
    passport_list[i] = passport
    i += 1

# Count valid passports
num_required_fields = 8
num_valid_passports = 0
for passport in passport_list:
    if len(passport) == num_required_fields:
        num_valid_passports += 1
    elif len(passport) == num_required_fields - 1:
        if not "cid" in passport:
            num_valid_passports += 1

print(num_valid_passports)
