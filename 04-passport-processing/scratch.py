valid_byr_range = range(1920, 2002 + 1)

dict = {"beep": "boop", "ding": "dong"}

# if dict["bing"] not in valid_byr_range:
#     print("failure")

string1 = "135in"
string2 = "33cm"

if string2[-2:] == "cm":
    print(string2[0:-2])

if int("2002") in valid_byr_range:
    print("range")