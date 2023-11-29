# Given a 2D integer array matrix, return the transpose of matrix.

# The transpose of a matrix is the matrix flipped over its main diagonal, 
# switching the matrix's row and column indices.

# time O(n*n) space O(n*n)
class Solution:
    def transpose(self, m):
        t = [[] for i in range(len(m[0]))]
        for i in range(len(m)): 
            for j in range(len(m[i])):
                t[j].append(m[i][j])
        return t      
        
s = Solution()

assert s.transpose([[1,2,3],[4,5,6],[7,8,9]]) == [[1,4,7],[2,5,8],[3,6,9]]
assert s.transpose([[1,2,3],[4,5,6]]) ==  [[1,4],[2,5],[3,6]]