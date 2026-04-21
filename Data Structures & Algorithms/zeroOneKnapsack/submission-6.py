#TODO do with 2 rows O(M) space
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N,M = len(profit), capacity
        prevRow = [0]*(M+1)
        # oh i need cal, what is the max for each capacity level , thats y we do this , for the row
        #setup first row and first col of all
        for i in range(M+1):
            if weight[0] <= i :
                prevRow[i] = profit[0]

        # Do DP , Find the best for each cell, if included , current c - weight check in row - 1 to see the best possible with that included, and row-1 skip , take max of that , we get max for each cell
        for i in range(1,N):
            curRow = [0]*(M+1)
            for j in range(M+1):
                # Skip 
                skip = prevRow[j]

                #include
                include = 0
                if j - weight[i]>=0:
                    include = profit[i] + prevRow[j-weight[i]]
                #Get Max of this
                curRow[j] = max(skip,include)
            prevRow = curRow
        return prevRow[M]