class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        hand.sort()
        for n in sorted(count.keys()):
            if count[n]>0:
                groupCount = count[n]
                for i in range(1,groupSize):
                    if count[n+i]<groupCount:
                        return False
                    count[n+i]-=groupCount
                count[n]=0
        return True