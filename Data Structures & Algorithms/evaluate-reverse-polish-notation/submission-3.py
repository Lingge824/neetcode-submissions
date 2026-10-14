class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for s in tokens:
            if s!="+" and s!="-" and s!="*" and s!="/":
                stack.append(int(s))
            else:
                if s=="+":
                    stack.append(stack.pop()+stack.pop())
                if s=="*":
                    stack.append(stack.pop()*stack.pop())
                if s=="/":
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(int(float(b)/a))
                if s=="-":
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(b-a)

        return stack.pop()