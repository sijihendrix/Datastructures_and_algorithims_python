"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('project_1/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('project_1/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def time_spent_on_phone(calls):
    max_time =  0
    number = ''
    for call in calls:
        if max_time < int(call[len(call) -1]):
            max_time = int(call[len(call) -1])
            number = call[0]

    return(max_time, number)

total_time, telephone_number = time_spent_on_phone(calls)

print(f'{telephone_number} spent the longest time, {total_time} seconds, on the phone during September 2016.')