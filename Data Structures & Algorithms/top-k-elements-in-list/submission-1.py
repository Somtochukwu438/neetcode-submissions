import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap = {}
        # for i in nums:
        #     if i in hashmap:
        #         hashmap[i] += 1
        #     else:
        #         hashmap[i] = 1
        # lis=[]
        # for i in range(k):
        #     max_e = max(hashmap, key = hashmap.get)
        #     lis.append(max_e)
        #     hashmap.pop(max_e)
        # return lis
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])
        for key, value in hashmap.items():
            bucket[value].append(key)
        res = []
        for j in range(len(bucket)-1, 0, -1):
            for a in bucket[j]:
                res.append(a)
                if len(res) == k:
                    return res
        return res


        



        