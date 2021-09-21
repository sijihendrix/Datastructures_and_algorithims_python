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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
 
 
def get_all_banglore_numbers(calls):
  called_by_banglore = []
  for call in calls:
    if '(080)' in call[0]:
      # print(call[0])
      called_by_banglore.append(call[1])
  
  return called_by_banglore

def get_area_code(arr):
  codes =  {}
  for i in range(len(arr)):
    if '(' in arr[i]:
      bracket_position = arr[i].find(')') + 1
      if arr[i][0: bracket_position] in codes:
        return
      codes.update({arr[i][0:bracket_position]: 1,})
      if arr[i][0:3] == "140":
          if arr[i][0:3] in codes:
            return
      # codes.update({arr[i][0:3]: 1})
    elif '(' not in arr[i]:
      mobile_prefix = arr[i][0:4]
      if mobile_prefix in codes:
          return
      codes.update({mobile_prefix: 1})
      print(codes)

    for k in codes.keys():
      print(k)
  return codes.key()


codes =    get_area_code(get_all_banglore_numbers(calls))

print(f"The numbers called by people in Bangalore have codes", codes)

# TODO fix mess above. Simplify it
