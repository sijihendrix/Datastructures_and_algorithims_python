# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    while isHigherDate(year1, month1, day1, year2, month2, day2) == True:
        year1,month1,day1 = nextDay(year1,month1,day1)
        days +=1
           
      
        
    # YOUR CODE HERE!
    return days

def isHigherDate(year1, month1, day1, year2, month2, day2):
    if year2 > year1:
        return True
    elif year2 == year1 and month2 > month1:
        return True
        
    elif year2 == year1 and month2 == month1:
        if day2 > day1:
            return True
    
    return False



def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print( "Test with data:", args, "failed")
        else:
            print ("Test case passed!")

test()
    