class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        suffix=1
        ans[0]=1
        for i in range(1,len(nums),1):
            ans[i]=ans[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            suffix*=nums[i+1]
            ans[i]*=suffix
        return ans

        