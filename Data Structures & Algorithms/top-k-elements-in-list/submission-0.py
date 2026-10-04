import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        lis=[]
        for i in range(k):
            max_e = max(hashmap, key = hashmap.get)
            lis.append(max_e)
            hashmap.pop(max_e)
        return lis


        



        