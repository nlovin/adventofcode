import re

with open('data/day3.txt', 'r') as file:
    memory = file.read()


matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', memory)

pairs = []

for match in matches:
    x = int(match[0])
    y = int(match[1])
    pairs.append([x,y])

total = 0

for pair in pairs:
    total += pair[0] * pair[1]

print(total)