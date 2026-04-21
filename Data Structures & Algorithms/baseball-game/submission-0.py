class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        prev = 0
        one,two = 0,0
        for op in operations:
            if op=='+':
                one,two = stack.pop(),stack.pop()
                stack.append(two)
                stack.append(one)
                stack.append(one+two)
            elif op == 'D':
                prev =stack.pop()
                stack.append(prev)
                stack.append(prev*2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)