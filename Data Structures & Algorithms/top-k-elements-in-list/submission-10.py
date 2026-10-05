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
        # hashmap = {}
        # for i in nums:
        #     if i in hashmap:
        #         hashmap[i] += 1
        #     else:
        #         hashmap[i] = 1
        # bucket = []

        # for i in range(len(nums) + 1):
        #     bucket.append([])
        # for num, freq in hashmap.items():
        #     bucket[freq].append(num)

        # res = []
        # for j in range(len(bucket) - 1, 0, -1):
        #     for num in bucket[j]:
        #         res.append(num)
        #         if len(res) == k:
        #             return res
        # return res
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        heap = []

        for num, freq in hashmap.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]

        


        
        









