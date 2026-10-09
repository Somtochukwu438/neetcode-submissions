class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""
        for i in s:
            if i.isalnum():
                x+=i.lower()
        if x == x[::-1]:
            return True
        return False
