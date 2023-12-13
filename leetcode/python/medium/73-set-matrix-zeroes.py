# Given an m x n integer matrix matrix, if an element is 0, 
# set its entire row and column to 0's.

# You must do it in place.

class Solution:
    def setZeroes(self, M):
        zeroes = set()
        for i in range (0, len(M)):
            for j in range (0,len(M[0])):
                if M[i][j] == 0: 
                    zeroes.add((i,j))
        for points in zeroes: 
            self.row(points[0], len(M[0]), M)
            self.col(points[1], len(M), M)
    
    def row(self, col, end, M): 
        for i in range(0, end): 
            M[col][i] = 0 

    def col(self, row, end, M): 
        for i in range(0, end):
            M[i][row] = 0

s = Solution()

m = [[1,1,1],[1,0,1],[1,1,1]]
s.setZeroes(m)
assert m == [[1,0,1],[0,0,0],[1,0,1]]

m = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s.setZeroes(m)
assert m == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

