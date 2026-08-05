class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        alphabet=[0]*200
        for i in range(len(s)):
            alphabet[ord(s[i])]+=1
            alphabet[ord(t[i])]-=1
        for i in alphabet:
            if i!=0:
                return False
        return True