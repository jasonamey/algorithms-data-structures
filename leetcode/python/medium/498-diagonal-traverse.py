# Given an m x n matrix mat, return an array of all the 
# elements of the array in a diagonal order.

class Solution:
    def findDiagonalOrder(self, mat):
        direction = "U"
        final = []
        x = 0 
        y = 0 
        while x != len(mat[0]) and y != len(mat):
            final.append(mat[y][x])
            if direction == 'U': 
                if x == len(mat[0]) - 1: 
                    y += 1 
                    direction = 'D'
                elif y > 0:
                    y -= 1 
                    x += 1 
                else: 
                    x += 1 
                    direction = 'D'
            else: 
                if y == len(mat) - 1: 
                    x += 1 
                    direction = 'U'
                elif x > 0: 
                    x -= 1 
                    y += 1 
                else: 
                    y += 1 
                    direction = 'U'
        return final 
    
s = Solution()

mat = [[1,2,3],[4,5,6],[7,8,9]]
assert s.findDiagonalOrder(mat) == [1,2,4,7,5,3,6,8,9]

mat = [[1,2],[3,4]]
assert s.findDiagonalOrder(mat) == [1,2,3,4]
