class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        left = 0
        right = (num_rows * num_cols) - 1

        while left <= right:
            mid = (left + right) //2

            rows = mid // num_cols
            cols = mid % num_cols

            if matrix[rows][cols] == target:
                return True
            elif matrix[rows][cols] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
        