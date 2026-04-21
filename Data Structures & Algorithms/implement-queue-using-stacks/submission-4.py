# Time Complexity: 
#   - push: O(1)
#   - pop / peek: Amortized O(1). In the worst case it's O(N) when we have to pour, 
#                 but because each element is moved at most twice (once in, once out), 
#                 the AVERAGE time per operation is O(1).
# Space Complexity: O(N) - For storing the elements in the two stacks.
# Approach: Two Stacks (In-Stack and Out-Stack)

class MyQueue:
    def __init__(self):
        # s1 handles all incoming pushes
        self.s1 = []
        # s2 handles all outgoing pops/peeks
        self.s2 = []

    def push(self, x: int) -> None:
        # Pushing is now an instant O(1) operation!
        self.s1.append(x)

    def pop(self) -> int:
        # We must ensure s2 has the elements in the correct reversed order
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        # If the out-stack is empty, we must "pour" everything from s1 into s2.
        # Because stacks are LIFO, pouring from one to another perfectly reverses the order!
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        
        # The top of s2 is now the "front" of our queue
        return self.s2[-1]

    def empty(self) -> bool:
        # The queue is only empty if BOTH stacks are empty
        return not self.s1 and not self.s2