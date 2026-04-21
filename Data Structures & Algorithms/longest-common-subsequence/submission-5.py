class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N,M = len(text1), len(text2)
        if M>N:
            M,N= N,M
            text1,text2=text2,text1
        #M is small, small optimization for space
        dp = [0] * (M+1) #need the extra space on the left
        for i in range(N):
            curRow = [0] * (M+1)
            for j in range(M):
                if text1[i]==text2[j]:
                    curRow[j+1] = 1 + dp[j]
                else:
                    curRow[j+1] = max(dp[j+1],curRow[j])
            dp = curRow
        return dp[M]
