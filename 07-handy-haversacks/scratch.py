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
