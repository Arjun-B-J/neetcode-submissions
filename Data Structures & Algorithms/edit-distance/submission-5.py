class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word2)+1) for j in range(len(word1)+1)]
        #if empty string , the return len of other as base
        for i in range(len(word1)+1):
            dp[i][len(word2)] = len(word1)-i
        for j in range(len(word2)+1):
            dp[len(word1)][j] = len(word2)-j
        
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                #if same, just need to consider the next
                if word1[i]==word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    #if different take the best out of 3 ops
                    dp[i][j] = 1 + min(dp[i+1][j+1],dp[i][j+1],dp[i+1][j])

        return dp[0][0]




#   m o n k e y s 0               
# m 
# o
# n
# e
# y
# 0
