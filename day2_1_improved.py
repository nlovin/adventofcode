# A MUCH simpler revision. First attempt was a lot more work than was necessary.

def safety_check(report):
    asc = all(report[i+1]-report[i] >= 1 and report[i+1]-report[i] <= 3 for i in range(len(report) - 1))
    desc = all(report[i]-report[i+1] >= 1 and report[i]-report[i+1] <= 3 for i in range(len(report) - 1))

    if asc or desc:
        status = True
    else:
        status = False

    return status

# read in report data
reports = []
file_path = 'data/day2.txt'

with open(file_path, 'r') as file:
    for line in file:
        report = [int(item) for item in line.strip().split(' ')]  # Convert to integers
        reports.append(report)

# use safety checker
safe_reports = 0 
for report in reports:
    if safety_check(report):
        safe_reports += 1

# answer
print(safe_reports)