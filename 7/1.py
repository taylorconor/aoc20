import re

with open('7/input.txt') as f:
    data = f.read()


def find_children(bags, key):
    children = set()
    if key in bags:
        for child in bags[key]:
            children.add(child)
            children = children.union(find_children(bags, child))
    return children


inverted_bags = {}
outer_regex = r"([a-z\ ]+) bags contain (.*)."
inner_regex = r"(\d+)\ ([a-z\ ]+) b"
for outer_match in re.findall(outer_regex, data):
    for inner_match in re.findall(inner_regex, outer_match[1]):
        if not inner_match[1] in inverted_bags:
            inverted_bags[inner_match[1]] = set()
        inverted_bags[inner_match[1]].add(str(outer_match[0]))

children = find_children(inverted_bags, "shiny gold")
print(len(children))
