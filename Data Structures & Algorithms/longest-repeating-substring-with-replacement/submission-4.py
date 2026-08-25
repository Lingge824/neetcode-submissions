class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp=defaultdict(int)
        l=0
        ans=0
        maxfrequency=0
        for r in range(len(s)):
            mp[s[r]]=mp[s[r]]+1
            maxfrequency=max(maxfrequency,mp[s[r]])
            while r-l+1-maxfrequency>k:
                mp[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans