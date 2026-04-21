from typing import List, Optional

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # 1-indexed heap: index 0 unused
        self.heap: List[int] = [0]
        # build heap by inserting elements while keeping size <= k
        for x in nums:
            self.push(x)
            if len(self.heap) - 1 > self.k:
                self.pop()

    def push(self, val: int) -> None:
        """Insert val into min-heap (1-indexed)."""
        self.heap.append(val)
        i = len(self.heap) - 1
        # percolate up while parent is larger (min-heap invariant)
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

    def pop(self) -> Optional[int]:
        """Remove and return root (smallest element). Return None if empty."""
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        res = self.heap[1]
        # move last element to root and percolate down
        self.heap[1] = self.heap.pop()
        i = 1
        n = len(self.heap)
        while 2 * i < n:
            left = 2 * i
            right = left + 1
            # choose smaller child
            child = left
            if right < n and self.heap[right] < self.heap[left]:
                child = right
            # if heap[i] is greater than smaller child, swap
            if self.heap[i] > self.heap[child]:
                self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
                i = child
            else:
                break
        return res

    def heapify(self, arr: List[int]) -> None:
        """Build heap from given list (replaces current heap)."""
        # create 1-indexed array copy
        self.heap = [0] + list(arr)
        n = len(self.heap)
        # percolate down from last parent down to root
        cur = (n - 1) // 2
        while cur >= 1:
            i = cur
            while 2 * i < n:
                left = 2 * i
                right = left + 1
                child = left
                if right < n and self.heap[right] < self.heap[left]:
                    child = right
                if self.heap[i] > self.heap[child]:
                    self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
                    i = child
                else:
                    break
            cur -= 1

    def add(self, val: int) -> Optional[int]:
        """Add val and return the k-th largest (root of min-heap of size k)."""
        self.push(val)
        # keep heap size at most k
        if len(self.heap) - 1 > self.k:
            self.pop()
        # if there are no elements, return None; otherwise root is k-th largest (or current min if < k elements)
        return None if len(self.heap) == 1 else self.heap[1]
