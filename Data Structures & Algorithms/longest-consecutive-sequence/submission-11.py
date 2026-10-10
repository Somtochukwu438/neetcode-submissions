class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        s = list(nums)
        s.sort()
        ma = []
        count = 1
        j = 1

        for x in s:
            if j == len(s):
                break
            elif s[j] - x == 1:
                count += 1
                j += 1
            else:
                ma.append(count)
                count = 1
                j += 1
        ma.append(count)
        return max(ma)
        