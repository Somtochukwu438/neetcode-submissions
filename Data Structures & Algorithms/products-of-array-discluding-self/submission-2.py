import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = math.prod(nums)
        lis = []

        zero = nums.count(0)
        for i in nums:
            if zero > 1:
                lis.append(0)
            elif i == 0:
                s = []
                for x in nums:
                    if x != 0:
                        s.append(x)
                product = math.prod(s)
                lis.append(product)
            else:
                lis.append(int(result//i))
        return lis