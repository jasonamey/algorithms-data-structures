def revealMinesweeper(board, row, column):
  neighbors = getNeighbors(board, row, column)


  def getNeighbors(board, row, column):
    neighbors = []
    directions = [(-1,-1), (-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for y, x in directions: 
      
      if row >= 0 and row < len(board) and col >= 0 and col < len(board[0]): 
        neighbors.append((row, col))
    