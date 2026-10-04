class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for index in range(len(strs)):
            word = "".join(sorted(strs[index]))

            if word in hashmap:
                hashmap[word].append(strs[index])
            else:
                hashmap[word] = [strs[index]]
        
        res = []
        for value in hashmap.values():
            res.append(value)
        return res
