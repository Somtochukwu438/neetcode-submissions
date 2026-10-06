class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])
        for key, freq in hashmap.items():
            bucket[freq].append(key)
        lis = []
        for x in range(len(bucket)-1, 0, -1):
            for j in bucket[x]:
                lis.append(j)
                if len(lis) == k:
                    return lis
        return lis

        