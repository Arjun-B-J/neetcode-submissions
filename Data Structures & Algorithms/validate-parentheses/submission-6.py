class Solution:
    def isValid(self, s: str) -> bool:
        maps = {'(':')','{':'}','[':']'}
        stack = []
        for c in s:
            if c in maps.keys():
                stack.append(c)
            else:
                if len(stack) == 0 or c != maps[stack.pop()]:
                    return False
        if len(stack) == 0:
            return True
        return False
        