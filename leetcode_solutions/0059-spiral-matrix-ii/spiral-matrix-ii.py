# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# Example:
#
#
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
#
#


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        A = []
        lo = n*n + 1
        while lo > 1:
            
            lo, hi = lo - len(A), lo
            A = [list(range(lo,hi))] + [*zip(*A[::-1])]
            
        return [list(i) for i in A]
