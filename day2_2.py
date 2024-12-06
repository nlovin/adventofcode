# part 1 function
def safety_check(report):
    asc = all(report[i+1]-report[i] >= 1 and report[i+1]-report[i] <= 3 for i in range(len(report) - 1))
    desc = all(report[i]-report[i+1] >= 1 and report[i]-report[i+1] <= 3 for i in range(len(report) - 1))

    if asc or desc:
        status = True
    else:
        status = False

    return status

# part 2 function
def problem_dampener(report):
    if safety_check(report):
        return True
    else:
        for i in range(len(report)):
            if safety_check(report[:i]+report[i+1:]):
                return True
                break
            else:
                pass
        
        return False
    
# read in data
reports = []

file_path = 'data/day2.txt'

with open(file_path, 'r') as file:
    for line in file:
        report = [int(item) for item in line.strip().split(' ')]  # Convert to integers
        reports.append(report)

# run new function to catch more safe reports
safe_reports=0

for report in reports:
    #print(report)
    if problem_dampener(report):
        safe_reports += 1

print(safe_reports)