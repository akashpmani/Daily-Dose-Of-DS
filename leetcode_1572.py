"""
LEETCODE 1572 : MATRIX DIAGONAL SUM
------------------------------------
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

"""

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l = len(mat[0])
        e =  l-1
        s = i = 0
        sum = 0 
        while s < l and i < l and e >= 0:
            lis = mat[i]
            if s==e and s == i:
                sum +=lis[s]
            else:   
                sum += lis[e] + lis[s]
            e -= 1
            i += 1
            s += 1


        return sum

