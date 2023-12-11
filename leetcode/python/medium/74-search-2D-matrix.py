# You are given an m x n integer matrix matrix with the following 
# two properties:

# Each row is sorted in non-decreasing order.

# The first integer of each row is greater than the last integer 
# of the previous row.

# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

class Solution:
    def searchMatrix(self, matrix, target):
        y = 0 
        x = len(matrix[0]) - 1
        test = matrix[y][x]
        if test == target: 
            return True
        while (x > 0 and y < len(matrix)): 
            if test > target: 
                x = x - 1
                if x >= 0: 
                    test = matrix[y][x]
                    if test == target: 
                        return True 
                else: 
                    return False 
            else:
                y = y + 1
                if y < len(matrix): 
                    test = matrix[y][x]
                    if test == target: 
                        return True
                else: 
                    return False  
        return False 
        
s = Solution()

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target = 3
assert s.searchMatrix(matrix, target) == True 

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target = 13

assert s.searchMatrix(matrix, target) == False 