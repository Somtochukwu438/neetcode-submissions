class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        s = list(nums)
        new_s = sorted(s)

        count = 1
        j = 1
        main = []
        for x in new_s:
            if j == len(new_s):
                break
            elif new_s[j] - x == 1:
                count += 1
                j += 1
            else:
                main.append(count)
                j += 1
                count = 1
        main.append(count)
        return max(main)
        
        