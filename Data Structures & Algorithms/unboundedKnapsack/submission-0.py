class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        prevRow = [0]*(capacity+1)
        for i in range(len(profit)):
            curRow = [0]*(capacity+1)
            for j in range(1,capacity+1):
                skip = prevRow[j]
                newCap = j-weight[i]
                include = 0
                if newCap>=0:
                    include = profit[i]+curRow[j-weight[i]] #Cur Row itself cause we can choose the same item unlimited time
                curRow[j] = max(skip,include)
            prevRow = curRow
        return curRow[capacity]