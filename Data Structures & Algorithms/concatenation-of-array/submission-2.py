class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new = [0] * (2 * len(nums))

        for i,num in enumerate(nums):
            new[i] = new[i + len(nums)] = num
        return new        