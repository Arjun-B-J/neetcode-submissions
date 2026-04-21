class SegmentNode:
    def __init__(self, total, L, R):
        self.total = total  # Sum of all elements in range [L, R]
        self.L = L          # Left boundary of this node's range
        self.R = R          # Right boundary of this node's range
        self.left = None    # Left child — covers [L, M]
        self.right = None   # Right child — covers [M+1, R]


class SegmentTree:

    def build(self, nums, L, R):
        # Base case: leaf node represents a single element
        if L == R:
            return SegmentNode(nums[L], L, R)

        M = (L + R) // 2
        root = SegmentNode(0, L, R)

        # Recursively build left and right subtrees
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M + 1, R)

        # Internal node's total is the sum of its two children
        root.total = root.left.total + root.right.total
        return root

    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)

    def updateTree(self, root, index, val):
        # Base case: reached the leaf node for this index
        if root.L == root.R:
            root.total = val
            return

        M = (root.L + root.R) // 2

        # Recurse into whichever child contains the target index
        if index > M:
            self.updateTree(root.right, index, val)
        else:
            self.updateTree(root.left, index, val)

        # Recompute this node's total on the way back up
        root.total = root.left.total + root.right.total

    def update(self, index: int, val: int) -> None:
        self.updateTree(self.root, index, val)

    def queryTree(self, root, L, R):
        # Exact match — this node's range is exactly what we need
        if root.L == L and root.R == R:
            return root.total

        M = (root.L + root.R) // 2

        if L > M:
            # Query range is entirely in the right subtree
            return self.queryTree(root.right, L, R)
        elif R <= M:
            # Query range is entirely in the left subtree
            return self.queryTree(root.left, L, R)
        else:
            # Query range spans both children — split and sum
            # Left half:  [L, M]
            # Right half: [M+1, R]
            return (self.queryTree(root.left, L, M) +
                    self.queryTree(root.right, M + 1, R))

    def query(self, L: int, R: int) -> int:
        return self.queryTree(self.root, L, R)
        