class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j,k = 0,0,0
        w1,w2 = len(word1),len(word2)
        ans = ""
        while i<w1 and j<w2:
            if k%2==0:
                ans+=word1[i]
                i+=1
                k+=1
            else:
                ans+=word2[j]
                j+=1
                k+=1
        ans = ans + word1[i:]+word2[j:]
        return ans