class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        glo_max = nums[0]
        glo_min = nums[0]
        curr_max = 0
        curr_min = 0
        total = 0

        for num in nums:
            curr_max = max(curr_max + num, num)
            curr_min = min(curr_min + num, num)
            total += num
            glo_max = max(glo_max, curr_max)
            glo_min = min(glo_min, curr_min)
        return max(glo_max, total - glo_min) if glo_max > 0 else glo_max
        