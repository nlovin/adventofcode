from collections import defaultdict

with open('data/day5.txt', 'r') as f:
    lines = f.readlines()

pairs = [line.strip().split('|') for line in lines if '|' in line]
lists = [line.strip().split(',') for line in lines if ',' in line]

pairs = [(int(x), int(y)) for x, y in pairs]
lists = [[int(x) for x in lst] for lst in lists]


def create_ordering_rules(pairs):
    rules = defaultdict(set)
    for before, after in pairs:
        rules[before].add(after)
    return rules

def should_come_before(a, b, rules):
    # If a should come before b according to rules
    if b in rules.get(a, set()):
        return -1
    # If b should come before a according to rules
    if a in rules.get(b, set()):
        return 1
    # If no rule exists between these numbers
    return 0

def fix_ordering(lst, pairs):
    rules = create_ordering_rules(pairs)
    
    # Custom sort using the rules
    from functools import cmp_to_key
    fixed_list = sorted(lst, key=cmp_to_key(lambda x, y: should_come_before(x, y, rules)))
    
    return fixed_list

# Usage
fixed_lists = []
for lst in lists:
    fixed_list = fix_ordering(lst, pairs)
    fixed_lists.append(fixed_list)

middle_num_sum = 0

for lst in fixed_lists:
    middle_num_sum += lst[len(lst) // 2]

print(middle_num_sum) # subtract first sum