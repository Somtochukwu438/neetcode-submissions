class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic_1 = {}
        dic_2 = {}
 
        for i, j in zip(s, t):
            if i not in dic_1:
                dic_1[i] = 1
            else:
                dic_1[i] += 1
            
            if j not in dic_2:
                dic_2[j] = 1
            else:
                dic_2[j] += 1
        return dic_1 == dic_2
        