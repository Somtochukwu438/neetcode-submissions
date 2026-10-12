class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix[0]) - 1

        while start < len(matrix) and end >= 0:
            if matrix[start][end] == target:
                return True
            elif matrix[start][end] > target:
                end -= 1
            else:
                start += 1
        return False
        