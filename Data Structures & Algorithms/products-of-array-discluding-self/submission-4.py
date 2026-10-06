import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = math.prod(nums)
        res = []
        zero = nums.count(0)

        for i in nums:
            if zero > 1:
                res.append(0)
            elif i == 0:
                temp = []
                for x in nums:
                    if x!= 0:
                        temp.append(x)
                product = math.prod(temp)
                res.append(product)
            else:
                res.append(int(result//i))
        return res
        
        