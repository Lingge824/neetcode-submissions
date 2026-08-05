class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp={}
        for s in strs:
            c=[0]*26
            for char in s:
                c[ord(char)-ord('a')]+=1
            key=tuple(c)
            if key not in mp:
                mp[key]=[]
            mp[key].append(s)
        return list(mp.values())