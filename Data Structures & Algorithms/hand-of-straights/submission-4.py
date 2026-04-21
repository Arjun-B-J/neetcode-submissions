from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Base case: if total cards aren't divisible by groupSize, it's impossible.
        if len(hand) % groupSize != 0:
            return False
        
        # Count frequencies of each card
        count = Counter(hand)
        hand.sort()
        # Iterate through the unique cards in ascending order
        for num in hand:
            if count[num] > 0:
                # The number of groups we must start with this 'num'
                start_count = count[num]
                
                # Check and decrement the required consecutive cards
                for i in range(num, num + groupSize):
                    if count[i] < start_count:
                        return False # Not enough of card 'i' to complete the group
                    
                    count[i] -= start_count
                    
        return True