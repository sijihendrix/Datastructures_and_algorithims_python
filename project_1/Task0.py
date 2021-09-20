"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('project_1/texts.csv') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('project_1/calls.csv') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
def retrieve_text_details(texts, i = 1):

    incoming_number, answering_number, time = [i  for i in texts[i]]
        
    return incoming_number, answering_number, time

incoming_number, answering_number, time = retrieve_text_details(texts)


print(f'First record of texts, {incoming_number} texts {answering_number} at time {time} ')


def retrieve_call_details(calls, i = 1):

    i = len(calls) -1

    incoming_number, answering_number, time, during  = [i  for i in calls[i]]
    
        
    return incoming_number, answering_number, time, during


incoming_number, answering_number, time, during = retrieve_call_details(calls)



print(f'Last record of calls, {incoming_number} calls {answering_number} at time {time}, lasting {during} seconds')