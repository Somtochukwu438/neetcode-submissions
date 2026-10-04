class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new = []

        for i in range(2):
            for n in nums:
                new.append(n)
        return new
        