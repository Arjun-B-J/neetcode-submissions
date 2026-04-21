class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        stack = []
        valid = True
        for c in s:
            if c in ['(','[','{']:
                stack.append(c)
            elif c=='}':
                if not stack or len(stack)<1 or stack[-1]!='{':
                    valid=False
                    break
                else:
                    stack.pop()
            elif c==')':
                if not stack or len(stack)<1 or stack[-1]!='(':
                    valid=False
                    break
                else:
                    stack.pop()
            elif c==']':
                if not stack or len(stack)<1 or stack[-1]!='[':
                    valid=False
                    break
                else:
                    stack.pop()
        if len(stack)>0:
            return False
        return valid

        