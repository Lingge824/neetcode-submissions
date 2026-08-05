class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        ans[0]=1
        suffix=1
        for i in range(1,len(ans),1):
            ans[i]=ans[i-1]*nums[i-1]
        for i in range(len(ans)-1,-1,-1):
            ans[i]*=suffix
            suffix*=nums[i]
        return ans