class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for x in nums:
            if (x-1) not in num_set:
                current_num = x
                current_streak = 1

                while (current_num+1) in num_set:
                    current_streak += 1
                    current_num += 1
                longest_streak = max(current_streak, longest_streak)
        return longest_streak
