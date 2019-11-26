from . import db
  
def notInRow(arr, row):  
    st = set()  
  
    for i in range(0, 9):  
  
        if arr[row][i] in st:  
            return False
  
        if arr[row][i] != 0:  
            st.add(arr[row][i])  
      
    return True
  
# Checks whether there is any  
# duplicate in current column or not.  
def notInCol(arr, col):  
  
    st = set()  
  
    for i in range(0, 9):  
  
        if arr[i][col] in st: 
            return False
  
        if arr[i][col] != 0:  
            st.add(arr[i][col])  
      
    return True
  
# Checks whether there is any duplicate in sub grid 
def notInBox(arr, startRow, startCol):  
  
    st = set()  
  
    for row in range(0, 3):  
        for col in range(0, 3):  
            curr = arr[row + startRow][col + startCol]  
  
            # If already encountered before,  
            # return false  
            if curr in st:  
                return False
  
            # If it is not an empty cell,  
            # insert value at current cell in set  
            if curr != 0:  
                st.add(curr)  
          
    return True
  
# Checks whether current row and current  
# column and current 3x3 box is valid or not  
def isValid(arr, row, col):  
  
    return (notInRow(arr, row) and notInCol(arr, col) and
            notInBox(arr, row - row % 3, col - col % 3))  
  
  
def isValidConfig(arr, n):  
  
    for i in range(0, n):  
        for j in range(0, n):  
  
            if not isValid(arr, i, j):  
                return False
          
    return True
  
def make_input_arr(input_str):
    db_instance = db.get_db()
    print(input_str)
    try:
        db_instance.execute(
                'INSERT INTO sudoku_pattern(pattern) VALUES (?)',(input_str,)
            )
    except Exception as e:
        pass
    db_instance.commit()
    db_instance.close()
    input_list = []
    temp_list = []
    input_str = input_str.replace(".","0")

    for idx,value in enumerate(input_str):
        if((idx+1)%9==0):
            temp_list.append(int(value))
            input_list.append(temp_list)
            temp_list = []
        else:
            temp_list.append(int(value))
    return input_list

#print(make_input_arr("4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"))
# # Drivers code  
# if __name__ == "__main__": 
  
#     board = [['4', '.', '.', '.', '.', '.', '8', '.', '5'], 
#              ['.', '3', '.', '.', '.', '.', '.', '.', '.'], 
#              ['.', '.', '.', '7', '.', '.', '.', '.', '.'], 
#              ['.', '2', '.', '.', '.', '.', '.', '6', '.'], 
#              ['.', '.', '.', '.', '8', '.', '4', '.', '.'], 
#              ['.', '.', '.', '.', '1', '.', '.', '.', '.'], 
#              ['.', '.', '.', '6', '.', '3', '.', '7', '.'], 
#              ['5', '.', '.', '2', '.', '.', '.', '.', '.'], 
#              ['1', '.', '4', '.', '.', '.', '.', '.', '.']]
          
#     if isValidConfig(board, 9):  
#         print("YES") 
#     else: 
#         print("NO") 
  
# # This code is contributed by Rituraj Jain
  