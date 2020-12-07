import re

with open('7/input.txt') as f:
    data = f.read()


def sum_children(bags, key):
    result = 0
    if key in bags:
        for child in bags[key]:
            result += bags[key][child] * (1 + sum_children(bags, child))
    return result


bags = {}
outer_regex = r"([a-z\ ]+) bags contain (.*)."
inner_regex = r"(\d+)\ ([a-z\ ]+) b"
for outer_match in re.findall(outer_regex, data):
    for inner_match in re.findall(inner_regex, outer_match[1]):
        if not outer_match[0] in bags:
            bags[outer_match[0]] = {}
        bags[outer_match[0]][inner_match[1]] = int(inner_match[0])

print(str(sum_children(bags, "shiny gold")))
