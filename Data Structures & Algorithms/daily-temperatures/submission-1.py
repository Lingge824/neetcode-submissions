class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        length=len(temperatures)
        result=[0]*length
        for i in range(length-1,-1,-1):
            while stack and stack[-1][0]<=temperatures[i]:
                stack.pop()
            if stack:
                result[i]=stack[-1][1]-i
            stack.append((temperatures[i],i))
        return result
