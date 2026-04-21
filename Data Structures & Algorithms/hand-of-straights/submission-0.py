class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        #sort and try to arrange into groups greedily
        hand.sort()
        used = {}
        i=0
        while len(used)!=len(hand):
            while i in used: #find the group first ele
                i+=1
            if i>=len(hand):
                    return False
            used[i]=True
            print(used[i],hand[i])
            prev = hand[i]
            l=1
            i+=1
            while l<groupSize:
                while i<len(hand) and (i in used or hand[i]==prev): #find the next ele
                    i+=1
                if i>=len(hand):
                    return False
                print(i,prev,hand[i])
                if prev+1 != hand[i]:
                    return False
                else:
                    prev = hand[i]
                    used[i]=True
                l+=1
            i=0
        
        return True

