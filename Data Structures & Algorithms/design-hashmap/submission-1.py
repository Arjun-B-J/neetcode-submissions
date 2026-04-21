# ==========================================
# Approach 2: Direct Indexing (Massive Array)
# Time Complexity: O(1) absolute time for all operations.
# Space Complexity: O(M) where M is the maximum possible key (1,000,001).
# Why this works here: The constraints explicitly state 0 <= key <= 1,000,000.
# ==========================================
class MyHashMap:
    def __init__(self):
        # Initialize an array of size 1,000,001 with -1
        # -1 represents an "empty" slot since the problem says 0 <= value.
        self.map = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1