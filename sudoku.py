sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
print("- - - - - - - - - - -")
for row in range (9):
  for column in range(9):
    if column == 2 or column == 5:
      print(sudoku[row][column],"|",end = " ")
    else:
      print(sudoku[row][column],end = " ")
    if column == 8:
      print(" ")
  if row == 2 or row == 5 or row == 8:
    print("- - - - - - - - - - -")
    



