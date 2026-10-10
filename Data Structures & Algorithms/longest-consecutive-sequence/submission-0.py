class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        s = list(nums)
        s.sort()

        ma = []
        j = 1
        count = 1
        for i in s:
            if j == len(s):
                break
            elif s[j] - i == 1:
                count += 1
                j += 1
            else:
                ma.append(count)
                count = 1
                j += 1
        ma.append(count)
        return max(ma)
        