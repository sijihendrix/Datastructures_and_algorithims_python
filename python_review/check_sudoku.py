correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
# Define a function check_sudoku() here:
def check_sudoku(sudoku):
    
    for i in range(len(sudoku)):
        map = set()
        for j in range(1, len(sudoku[i]) + 1):
            if j not in sudoku[i]:
                return False
            if sudoku[j-1][i] not in map:
                map.add(sudoku[j-1][i])
            else:
                return False
    return True




    
    
print(check_sudoku(incorrect))
#>>> False

# print(check_sudoku(correct))
#>>> True

# print(check_sudoku(incorrect2))
#>>> False

# print(check_sudoku(incorrect3))
#>>> False

# print(check_sudoku(incorrect4))
#>>> False

# print(check_sudoku(incorrect5))
#>>> False
