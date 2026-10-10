class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_s = set(nums)
        longest = 0

        for i in num_s:
            if (i-1) not in num_s:
                curr = i
                streak = 1

                while (curr + 1) in num_s:
                    streak += 1
                    curr += 1
                longest = max(longest, streak)
        return longest
        
        