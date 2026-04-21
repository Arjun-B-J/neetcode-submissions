# Time Complexity: O(m * n) - Each coordinate is computed at most once and then cached.
# Space Complexity: O(m * n) - Space is used by the recursion stack and the memoization dictionary.
# Approach: Top-Down Dynamic Programming (Recursion with Memoization)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}                                               # Cache to store computed paths for each coordinate
        
        def dfs(r, c):
            if r == m - 1 and c == n - 1:                       # Base case: Successfully reached the destination
                return 1
            if r >= m or c >= n:                                # Base case: Out of bounds (hit a wall)
                return 0
            if (r, c) in memo:                                  # Prune tree: Return already computed paths for this cell
                return memo[(r, c)]
            
            # Choice: Move DOWN (r+1) or move RIGHT (c+1)
            memo[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return memo[(r, c)]                                 # Cache and bubble up the total unique paths
            
        return dfs(0, 0)                                        # Start traversing from the top-left corner