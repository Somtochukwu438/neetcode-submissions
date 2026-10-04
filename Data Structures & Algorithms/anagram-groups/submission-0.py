class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        new_dict = {}

        for i in range(len(strs)):
            word = "".join(sorted(strs[i]))
            if word in new_dict:
                new_dict[word].append(strs[i])
            else:
                new_dict[word] = [strs[i]]
        
        res = []
        for value in new_dict.values():
            res.append(value)

        return res
        