import re

with open('data/day3.txt', 'r') as file:
    memory = file.read()

match_pattern = re.compile(r"do\(\)|don't\(\)|mul\(\d+,\d+\)")
num_pattern = re.compile(r"\d+")

do = True
total = 0

for match in match_pattern.findall(memory):
    if match == "do()":
        do = True
    elif match=="don't()":
        do = False
    elif do:
        tmp = num_pattern.findall(match)
        total += int(tmp[0]) * int(tmp[1])



print(total)
