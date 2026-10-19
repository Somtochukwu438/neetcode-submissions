class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n:
            temp = 0
            for num in str(n):
                temp += int(num)**2
            if temp == 1:
                return True
            elif temp in seen:
                return False
            seen.add(temp)
            n = temp


        