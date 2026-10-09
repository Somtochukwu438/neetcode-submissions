import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = math.prod(nums)
        zero = nums.count(0)

        res = []
        for i in nums:
            if zero > 1:
                res.append(0)
            elif i == 0:
                temp = []
                for x in nums:
                    if x != 0:
                        temp.append(x)
                res.append(math.prod(temp))
            else:
                res.append(int(result//i))
        return res

        
        