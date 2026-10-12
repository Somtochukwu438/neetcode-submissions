class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max_area = 0

        while start < end:
            width = end - start
            height = min(heights[end], heights[start])
            area = width * height
            max_area = max(max_area, area)
            if heights[end] > heights[start]:
                start += 1
            else:
                end -= 1
        return max_area
        