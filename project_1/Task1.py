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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# print(calls, texts)

def number_of_uniq_telelphones(texts, calls):

    count =  0
    numbers = {}
    for i in range(len(texts)):
        for j in range(2):
            if texts[i][j] in numbers:
                pass
            else:
                
                numbers.update({texts[i][j]:1})
                count +=1    
    
    for i in range(len(calls)):
        for j in range(2):
            if calls[i][j] in numbers:
                pass
            else:
                
                numbers.update({calls[i][j]:1})
                count +=1   
    return count


print(number_of_uniq_telelphones(texts, calls) )