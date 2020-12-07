import re


def get_containers(color, rules):
    containers = set()
    for rule in rules:
        if re.match(".*contain.*" + color, rule):
            container = rule.split(" bags contain")[:1][0]
            containers.add(container)
            containers = containers.union(get_containers(container, rules))
    return containers


with open("input.txt", "r") as f:
    rules = f.read().splitlines()

color = "shiny gold"
result = get_containers(color, rules)
print(len(result))