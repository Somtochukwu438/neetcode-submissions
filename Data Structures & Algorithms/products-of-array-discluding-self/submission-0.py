import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = math.prod(nums)
        lis = []

        zero_count = nums.count(0)

        for i in nums:
            if zero_count > 1:
                lis.append(0)

            elif i == 0:
                temp = []

                for x in nums:
                    if x != 0:
                        temp.append(x)

                product = math.prod(temp)
                lis.append(product)

            else:
                lis.append(int(result // i))
        return lis