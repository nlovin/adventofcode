from collections import defaultdict

with open('data/day5.txt', 'r') as f:
    lines = f.readlines()

pairs = [line.strip().split('|') for line in lines if '|' in line]
lists = [line.strip().split(',') for line in lines if ',' in line]

pairs = [(int(x), int(y)) for x, y in pairs]
lists = [[int(x) for x in lst] for lst in lists]

def check_ordering(lst, pairs):
    # Create a dictionary of rules: {number: [numbers that must come after it]}
    rules = defaultdict(set)
    for before, after in pairs:
        rules[before].add(after)
    
    # For each pair of numbers in the list
    for i, num in enumerate(lst):
        # Look at all numbers that come after this one
        for after_num in lst[i+1:]:
            # If we have a rule where 'after_num' should come before 'num'
            # then this list violates our rules
            if num in rules.get(after_num, set()):
                return False
    return True


# Usage
valid_lists = []
for lst in lists:
    if check_ordering(lst, pairs):
        valid_lists.append(lst)

print(f"Found {len(valid_lists)} valid lists")

middle_num_sum = 0

for lst in valid_lists:
    middle_num_sum += lst[len(lst) // 2]

print(middle_num_sum)