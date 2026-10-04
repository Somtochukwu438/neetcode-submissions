class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new = [0] * (len(nums) * 2)
        idx = 0

        for i in nums:
            new[idx] = i
            idx += 1
        
        for i in nums:
            new[idx] = i
            idx += 1
        return new
