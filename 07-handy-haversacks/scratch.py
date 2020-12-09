colors = ["blue", "pink", "yellow"]
new_colors = ["green", "red", "grey"]

colors.extend(new_colors)
print(colors)

my_set = set()
my_set.add("boop")
my_set.add("boop")
my_set.add("beep")
new_set = set()
new_set.add("blorp")
my_set = my_set.union(new_set)
print(my_set)

string = "shiny gold bags contain 5 bright maroon bags, 5 shiny aqua bags, 2 clear lime bags, 2 muted white bags."
# string = string.split(" bags, ")
# string[-1] = string[-1][:-6]
# string[0] = string[0].split(" ")[-3:]
# string[0] = " ".join(string[0])
# print(string)
# print("words"[2:])

import re

color = "shiny gold"
if re.match(color + ".*contain [1-9]", string):
    print("matched")

color2 = "bright maroon"
string2 = "bright maroon bags contain 4 faded indigo bags."
if re.match(color2 + ".*contain [1-9]", string2):
    print("matched single")

color3 = "light cyan"
string3 = "light cyan bags contain no other bags."
if re.match(color3 + ".*contain [1-9]", string3):
    print("matched no other bags")
else:
    print(1)

dumb_list = ["2 dim green bags."]
print(dumb_list[-1])

if re.match(".*no other bags.", string3):
    print("re matched no other bags correctly")