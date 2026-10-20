class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxA=0

        for i,h in enumerate(heights):
            start=i

            while stack and stack[-1][1]>h:
                ind,hei=stack.pop()
                start=ind
                maxA=max(maxA, (i-ind)*hei)

            stack.append([start,h])
        for ind, hei in stack:
            maxA=max(maxA, (len(heights)-ind)*hei)
        return maxA
           
            
