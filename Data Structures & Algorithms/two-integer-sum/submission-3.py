class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lis = []
        for index, item in enumerate(nums):
            for i in range(index+ 1, len(nums)):
                if nums[index] + nums[i] == target:
                    lis.append(index)
                    lis.append(i)
                    return lis
                
                
            

        
            


        