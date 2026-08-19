class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while r-l>0:
            while l < r and not self.validChar(s[l]):
                l+=1
            while r > l and not self.validChar(s[r]):
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            else:
                l+=1
                r-=1
        return True
    def validChar(self,c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))