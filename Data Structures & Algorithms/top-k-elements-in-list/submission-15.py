import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        heap = []
        for item, freq in hashmap.items():
            heapq.heappush(heap, (freq, item))
            if len(heap) > k:
                heapq.heappop(heap)
        lis = []
        for freq, item in heap:
            lis.append(item)
        return lis
        