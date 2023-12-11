# You are given an m x n integer matrix matrix with the following 
# two properties:

# Each row is sorted in non-decreasing order.

# The first integer of each row is greater than the last integer 
# of the previous row.

# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

class Solution:
    def searchMatrix(self, m, target):
        x = len(m[0]) - 1 
        y = 0
        while (x >= 0 and y < len(m)): 
            num = m[y][x]
            if num == target: 
                return True
            elif num < target: 
                y += 1
            else: 
                x -= 1 
        return False
s = Solution()

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target = 3
assert s.searchMatrix(matrix, target) == True 

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target = 13

assert s.searchMatrix(matrix, target) == False 