# Day 1!
# https://adventofcode.com/2024/day/1

# Find the distance between two lists

list1 = []
list2 = []

file_path = 'data/day1.txt'

with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split('   ') # why the heck is delim'd by 3 spaces
        list1.append(parts[0])
        list2.append(parts[1])


list1 = sorted(list1)
list2 = sorted(list2)

diff_list = []
for i in range(len(list1)):
    diff_list.append(abs(int(list1[i])-int(list2[i])))

total_distance = sum(diff_list)

print(total_distance)


# part 2

freq = {}

for item in list2:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

sim_score = []

for item in list1:
    if item in freq:
        sim_score.append(int(item) * freq[item])
    else:
        sim_score.append(0)

sum_sim = sum(sim_score)

print(sum_sim)
