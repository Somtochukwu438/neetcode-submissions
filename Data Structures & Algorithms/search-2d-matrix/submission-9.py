class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_row = len(matrix)
        num_col = len(matrix[0])

        left = 0
        right = (num_row * num_col) - 1

        while left <= right:
            mid = (left + right)//2

            row = mid // num_col
            col = mid % num_col
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
            

        