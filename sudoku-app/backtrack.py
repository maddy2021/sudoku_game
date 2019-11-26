# find Empty location in grid
def find_empty_location(arr,l): 
    for row in range(9): 
        for col in range(9): 
            if(arr[row][col]==0): 
                l[0]=row 
                l[1]=col 
                return True
    return False

# find duplicate in row
def find_in_row(arr,row,num): 
    for i in range(9): 
        if(arr[row][i] == num): 
            return True
    return False
  

# find duplicate in col
def find_in_col(arr,col,num): 
    for i in range(9): 
        if(arr[i][col] == num): 
            return True
    return False
  

# find duplicate in sub grid
def find_in_box(arr,row,col,num): 
    for i in range(3): 
        for j in range(3): 
            if(arr[i+row][j+col] == num): 
                return True
    return False
  
# check that number is safe to put
def check_location_is_safe(arr,row,col,num): 
      
    return not find_in_row(arr,row,num) and not find_in_col(arr,col,num) and not find_in_box(arr,row - row%3,col - col%3,num) 
  
# backtrack logic
def solve_sudoku(arr): 
      
    l=[0,0] 
      
    if(not find_empty_location(arr,l)): 
        return True
      
    row=l[0] 
    col=l[1] 
      
    for num in range(1,10): 
        if(check_location_is_safe(arr,row,col,num)): 
            arr[row][col]=num 
            if(solve_sudoku(arr)): 
                return True
            arr[row][col] = 0
    return False 


#make response string
def return_solution(grid):      
    print("grid is : ")
    print(grid)
    grid_data = grid    # if success print the grid 
    if(solve_sudoku(grid_data)): 
        return ''.join(str(item) for innerlist in grid_data for item in innerlist)
    else: 
        return "false"

# import validate
# data = validate.make_input_arr("53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79")
# print(data)
# print(return_solution(data))

