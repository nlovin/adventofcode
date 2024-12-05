# Day 2!
# https://adventofcode.com/2024/day/2

# Check if each line is only increasing or only decreasing and only by 1-3 each step

# Create a is_monotonic function
def is_monotonic(input_list):
    safety_status = []

    for index, list in enumerate(input_list):
        #print(index)
        #print("Starting")
        is_safe=True
        break_reason = None

        if list[0]>list[1]:
            asc=False
        else:
            asc=True

        #print(asc)

        for i in range(len(list)-1):
            if list[i]>list[i+1] and asc==True:
                safety_status.append(0)
                is_safe=False
                break_reason = 'Was ascending, but went down'
                #print('It broke! We were going up, but now we are going down!')
                break
            elif list[i]<list[i+1] and asc==False:
                safety_status.append(0)
                is_safe=False
                break_reason = 'Was descending, but we up'
                #print('It broke! We were going down, but now we are going up!')
                break
            elif list[i]>list[i+1] and asc==False:
                pass #print('Going down for now...')
            elif list[i]<list[i+1] and asc==True:
                pass #print('Going up for now...')

            
            if is_safe==False:
                break
            elif abs(list[i]-list[i+1])>3:
                safety_status.append(0)
                is_safe=False
                delta = str(abs(list[i]-list[i+1]))
                break_reason = 'Changed by too much'
                #print(f'Ah dang, it broke! {delta} was too much of a change!')
                break
            elif list[i]==list[i+1]:
                safety_status.append(0)
                is_safe=False
                break_reason = 'No change'
                break
            elif abs(int(list[i])-int(list[i+1]))<=3:
                pass
                #print("Whew...looks like we're good.")
            
        if is_safe == True:
            #print('We made it!')
            break_reason = 'We made it!'
            safety_status.append(1)
        
        #print('Break reason: ' + break_reason)
        

    #print(safety_status)
    #print(sum(safety_status))
    return safety_status


reports = []

file_path = 'data/day2.txt'


"""with open(file_path, 'r') as file:
    for line in file:
        report = line.strip().split(' ') 
        reports.append(report)
"""
with open(file_path, 'r') as file:
    for line in file:
        report = [int(item) for item in line.strip().split(' ')]  # Convert to integers
        reports.append(report)
            
#print(reports[0:2])
#print(reports[500:505])

x = is_monotonic(reports)

print(sum(x))
