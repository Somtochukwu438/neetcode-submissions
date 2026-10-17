class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_s = set(nums)
        streak = 0
        max_streak = 0

        for x in nums:
            if x - 1 not in num_s:
                curr_num = x
                streak = 1
                while curr_num + 1 in num_s:
                    curr_num += 1
                    streak += 1
                max_streak = max(streak, max_streak)
        return max_streak


        