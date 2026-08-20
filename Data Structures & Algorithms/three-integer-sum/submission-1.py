class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i,a in enumerate(nums):
            if a>0:
                break
            l,r=i+1,len(nums)-1
            if i>0 and a==nums[i-1]:
                continue
            while l<r:
                sum=a+nums[l]+nums[r]
                if sum>0:
                    r-=1
                if sum<0:
                    l+=1
                if sum==0:
                    ans.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return ans
