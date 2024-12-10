with open('data/day5.txt', 'r') as f:
    lines = f.readlines()

pairs = [line.strip().split('|') for line in lines if '|' in line]
lists = [line.strip().split(',') for line in lines if ',' in line]

pairs = [(int(x), int(y)) for x, y in pairs]
lists = [[int(x) for x in lst] for lst in lists]
