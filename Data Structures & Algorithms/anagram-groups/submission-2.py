class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            s1 = "".join(sorted(s))
            if s1 in hashmap:
                hashmap[s1].append(s)
            else:
                hashmap[s1] = [s]
        
        res = []
        for value in hashmap.values():
            res.append(value)
        return res
        