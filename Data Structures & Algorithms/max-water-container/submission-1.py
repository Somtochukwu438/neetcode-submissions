class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            width = j - i
            height = min(heights[j], heights[i])
            area = width * height
            max_area = max(max_area, area)
            if heights[j] > heights[i]:
                i += 1
            else:
                j -= 1

        return max_area
        