"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('project_1/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('project_1/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

 
def get_all_telemarketers(calls):
  telemarketers = []
  for call in calls:
    if (call[0][0:3] == '140'):
        if call[0] in telemarketers:
            continue
        telemarketers.append(call[0])
  
  return telemarketers


print(get_all_telemarketers(calls))