def isValidSudoku(board):
  for i in range(len(board)):
    if not checkRow(i, board):
      return False
  
  for i in range(len(board)):
    if not checkColumn(i, board):
      return False
    
  for i in range(3): 
    for j in range(3):
      if not checkBox(i*3, i*3 + 3, j*3, j*3 + 3, board):
        return False
  return True
        
def checkRow(idx, board):
  s = set() 
  for i in range(0, len(board)):
    if board[idx][i] != '.':
      num = int(board[idx][i])
      if num in s:
        return False
      else:
        s.add(num)
  return True

def checkColumn(idx, board):
  s = set()
  for i in range(0, len(board)):
    if board[i][idx] != '.':
      num = int(board[i][idx])
      if num in s:
        return False
      else:
        s.add(num)
  return True

def checkBox(xStart, xEnd, yStart, yEnd, board):
    s = set()
    for l in range(yStart, yEnd):
        for m in range(xStart, xEnd):
            if board[l][m] != '.':
              num = int(board[l][m])
              if num in s:
                return False
              else: 
                s.add(num)
    return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

assert isValidSudoku(board) == True

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

assert isValidSudoku(board) == False