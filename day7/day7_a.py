import re
from collections import defaultdict

outer_regex = re.compile(r'(.+?) bags contain')
inner_regex = re.compile(r'\d+ (.+?) bags?[,.]')

with open("input.txt") as file:
    lines = file.read().rstrip("\n").split("\n")

inner_colors = defaultdict(set)

for line in lines:
    outer_color = outer_regex.match(line).group(1)
    for inner_color in inner_regex.findall(line):
        inner_colors[inner_color].add(outer_color)

def solve(color):
    return inner_colors[color] | {x for c in inner_colors[color] for x in solve(c)}

print(len(solve("shiny gold")))

