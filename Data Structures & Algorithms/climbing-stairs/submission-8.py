class Solution:
    def climbStairs(self, n: int) -> int:
        def solve(n,cache):
            if n==0:
                return 1
            if n<0:
                return 0
            if n in cache:
                return cache[n]
            cache[n] = solve(n-1,cache)+solve(n-2,cache)
            return cache[n]
        return solve(n,{})
        