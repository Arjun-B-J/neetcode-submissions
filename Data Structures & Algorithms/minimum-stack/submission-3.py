class MinStack:

    def __init__(self):
        self.s = []
        self.ms = []
        

    def push(self, val: int) -> None:
        self.s.append(val)
        self.ms.append(min(val, self.ms[-1] if len(self.ms)>0 else val ))

    def pop(self) -> None:
        self.s.pop()
        self.ms.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.ms[-1]
