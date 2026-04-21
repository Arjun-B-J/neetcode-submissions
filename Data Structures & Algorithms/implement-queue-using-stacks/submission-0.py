class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        tempStack = []
        while self.stack:
            tempStack.append(self.stack.pop())
        self.stack.append(x)
        while tempStack:
            self.stack.append(tempStack.pop())
    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return True if not self.stack else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()