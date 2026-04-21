class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #greedy choice
        #from the current idx, where can i go next which has more coverage
        i=0
        while True:
            n=nums[i]
            curCoverage = i+n
            print(i,n)
            if curCoverage>=len(nums)-1:
                return True
            go=i+n
            
            for j in range(i,i+n+1):
                if nums[j]+j>curCoverage:
                    go=j
                    curCoverage=nums[j]+j
            
            if go==i:
                return False
            i=go
        