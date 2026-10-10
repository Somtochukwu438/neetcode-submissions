class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for x in num_set:
            if (x-1) not in num_set:
                curr_num = x
                streak = 1

                while (curr_num+1) in num_set:
                    curr_num += 1
                    streak += 1
                longest = max(longest, streak)
        return longest
                


        