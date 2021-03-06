# In the following exercise you will finish writing smallest_positive which is a function that finds the 
# smallest positive number in a list.

def smallest_positive(in_list):
    #TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    min_number =  None
    for item in in_list:
        if min_number == None:
            min_number = item
        elif item > 0 and item < min_number:
            min_number = item
            
    return min_number

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

def smallest_positive_solution(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    smallest_pos = None
    for num in in_list:
        if num > 0:
            # Note: we use a logical "or" in this solution to form 
            # the conditional statement, although this was
            # not introduced above. 
            if smallest_pos == None or num < smallest_pos:
                smallest_pos = num
    return smallest_pos

# Test cases


