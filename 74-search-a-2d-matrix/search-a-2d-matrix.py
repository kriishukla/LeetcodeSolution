from typing import List

class Solution:
    def get_row(self, matrix, target):
        low = 0
        high = len(matrix) - 1

        while high > low:
            mid = (low + high) // 2
            if matrix[mid][0] <= target < matrix[mid + 1][0]:
                return mid
            elif matrix[mid][0] <= target and matrix[mid + 1][0] <= target:
                low = mid + 1
            else:
                high = mid - 1
        
        return high

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        x = self.get_row(matrix, target)
        low = 0
        high = len(matrix[0]) - 1

        while high >= low:
            mid = (high + low) // 2
            if matrix[x][mid] == target:
                return True
            elif matrix[x][mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False

