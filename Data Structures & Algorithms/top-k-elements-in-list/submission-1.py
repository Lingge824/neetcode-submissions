class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp={}
        for i in nums:
            mp[i]=mp.get(i,0)+1
        bucket=[[] for _ in range(len(nums)+1)]
        for num, fre in mp.items():
            bucket[fre].append(num)
        ans=[]
        for fre in range(len(bucket)-1,0,-1):
            for num in bucket[fre]:
                ans.append(num)
                if len(ans)==k:
                    return ans
