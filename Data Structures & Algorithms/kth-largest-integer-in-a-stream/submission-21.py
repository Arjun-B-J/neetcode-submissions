class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap: List[int] = [0]  # 1-indexed heap (index 0 unused)
        self.k = k
        self.heapify(nums)

    def push(self, val: int) -> None:
        """Insert val and percolate up (max-heap)."""
        self.heap.append(val)
        i = len(self.heap) - 1
        # for max-heap, parent < child -> swap
        while i > 1 and self.heap[i] > self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

    def pop(self) -> Optional[int]:
        """Remove and return root (maximum). Return None if heap empty."""
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        res = self.heap[1]
        # move last element to root and percolate down (max-heap)
        self.heap[1] = self.heap.pop()
        i = 1
        n = len(self.heap)
        while 2 * i < n:
            left = 2 * i
            right = left + 1
            # choose larger child
            child = left
            if right < n and self.heap[right] > self.heap[left]:
                child = right
            # if parent < larger child, swap
            if self.heap[i] < self.heap[child]:
                self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
                i = child
            else:
                break
        return res

    def heapify(self, arr: List[int]) -> None:
        """Build a 1-indexed max-heap from arr. If arr empty, heap stays [0]."""
        if not arr:
            self.heap = [0]
            return
        # 1-indexed copy
        self.heap = [0] + list(arr)
        n = len(self.heap)
        # percolate down from last parent to root
        cur = (n - 1) // 2
        while cur >= 1:
            i = cur
            while 2 * i < n:
                left = 2 * i
                right = left + 1
                # pick larger child for max-heap
                child = left
                if right < n and self.heap[right] > self.heap[left]:
                    child = right
                if self.heap[i] < self.heap[child]:
                    self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
                    i = child
                else:
                    break
            cur -= 1

    def add(self, val: int) -> Optional[int]:
        """
        Insert val, pop up to k times to get k largest values (last popped is k-th largest),
        then reinsert popped values to restore the heap.
        """
        self.push(val)

        temp: List[int] = []
        # pop up to k times (or until heap empty)
        for _ in range(self.k):
            x = self.pop()
            if x is None:
                break
            temp.append(x)

        ans = None
        if temp:
            ans = temp[-1]  # last popped is the k-th largest

        # reinsert popped items (in the same order) to restore heap
        for x in temp:
            self.push(x)

        return ans
