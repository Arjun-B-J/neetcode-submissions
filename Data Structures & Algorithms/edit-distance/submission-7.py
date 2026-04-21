class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = {}
        def dfs(i, j):
            #if null return non empty to fill it
            if i == m:
                return n - j
            if j == n:
                return m - i
            #memo
            if (i, j) in dp:
                return dp[(i, j)]
            #if same look for next one
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            #if not same, 1 opp + min of insert delete 
            else:
                        #delete            #insert
                res = min(dfs(i + 1, j), dfs(i, j + 1))
                res = min(res, dfs(i + 1, j + 1)) #replace
                dp[(i, j)] = res + 1
            return dp[(i, j)]

        return dfs(0, 0)