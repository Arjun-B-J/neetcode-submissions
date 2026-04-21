class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        relax = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                elif relax:
                    relax.pop()
                else:
                    return False
            elif c=="*":
                relax.append(i)
        
        while stack and relax:
            if stack[-1] < relax[-1]:
                stack.pop()
                relax.pop()
            else:
                break
        
        return not stack