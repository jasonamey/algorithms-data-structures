def revealMinesweeper(board, row, column):
    if board[row][column] == 'M':
        board[row][column] = 'X'
        return board
    
    neighbors = getNeighbors(board, row, column)
    
    surrounding_mines = 0

    for n_row, n_colum in neighbors: 
        if board[n_row][n_colum] == 'M':
            surrounding_mines += 1
    if surrounding_mines != 0: 
      board[row][column] = str(surrounding_mines)
   
    else: 
      board[row][column] = "0"
      for n_row, n_column in neighbors:
        if board[n_row][n_column] == 'H':
          revealMinesweeper(board, n_row, n_column)
    return board

def getNeighbors(board, row, column):
  neighbors = []
  moves = [(-1,-1), (-1,0),(-1,1),(0,-1), (0,1), (1, -1), (1,0),(1,1)]
  for row_move, column_move in moves:
    test_row = row_move + row
    test_column = column_move + column
       
    if (test_row >= 0 and test_row < len(board) and test_column >= 0 and test_column < len(board[0])):
      neighbors.append((test_row, test_column))
  return neighbors

board = [
   ["H","H", "H", "H", "M"],["H", "H", "M", "H", "H"],["H", "H", "H", "H", "H"],["H", "H", "H", "H", "H"]
   ]   

# b = [
#    ['0', '1', 'H', 'H', 'M'], 
#    ['0', '1', 'M', '2', '1'], 
#    ['0', '1', '1', '1', '0'], 
#    ['0', '0', '0', '0', '0']]

print(revealMinesweeper(board, 0, 0))