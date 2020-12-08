import re
from collections import defaultdict

outer_regex = re.compile(r'(.+?) bags contain')
inner_regex = re.compile(r'(\d+) (.+?) bags?[,.]')

with open("input.txt") as file:
    lines = file.read().rstrip("\n").split("\n")

outer_colors = defaultdict(list)

for line in lines:
    outer_color = outer_regex.match(line).group(1)
    for count, inner_color in inner_regex.findall(line):
        outer_colors[outer_color].append((int(count), inner_color))

def cost(color):
    return sum(count + count * cost(inner_color) for count, inner_color in outer_colors[color])

print(cost('shiny gold'))

