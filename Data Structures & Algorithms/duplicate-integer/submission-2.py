class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lis = []
        seen = False
        for i in nums:
            if i in lis:
                seen = True
            else:
                lis.append(i)
        return seen

        