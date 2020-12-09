import re


def count_contents(color, rules):
    contents = 0
    for rule in rules:
        if re.match(color + ".*contain.*", rule):
            if re.match(".*no other bags.", rule):
                return 0

            else:
                content_list = rule.split("contain ")[-1]
                content_list = content_list.split(", ")

                for i in range(len(content_list)):
                    cutoff = content_list[i].find(" bag")
                    content_list[i] = content_list[i][:cutoff]
                    bag_count = int(content_list[i][:1])
                    bag_color = content_list[i][2:]
                    contents += bag_count + bag_count * count_contents(bag_color, rules)

                return contents


with open("input.txt", "r") as f:
    rules = f.read().splitlines()

color = "shiny gold"
result = count_contents(color, rules)
print(result)
