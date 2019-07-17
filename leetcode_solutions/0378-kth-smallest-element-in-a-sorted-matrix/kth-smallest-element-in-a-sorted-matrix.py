# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
#
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
#
# Example:
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# return 13.
#
#
#
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ n2.


import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)
        ret = 0
        for _ in range(k):
            #print(heap)
            ret, i, j = heapq.heappop(heap)
            if j+1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
        return ret
