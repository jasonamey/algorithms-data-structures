#not complete
def transposeMatrix(matrix):
    COL_LEN = len(matrix)
    col_start = 1
    for row in range(len(matrix) - 1):
        col = col_start
        while (col < COL_LEN):
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp
            col += 1
        col_start += 1
    print(matrix)


m = [
    [1, 4, 5],
    [2, 5, 7],
    [3, 6, 8]
  ]
m2 = [
   [1,2]
  ]

transposeMatrix(m2)