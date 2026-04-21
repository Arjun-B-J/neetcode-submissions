class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] #to keep the fleets
        cars = [[p,s] for p,s in zip(position,speed)]
        for p,s in sorted(cars)[::-1]: #reverse order here, go from right to left
            stack.append((target-p)/s) #append the time it takes
            if len(stack)>=2 and stack[-1] <= stack[-2]: #if the cur which we append is taking less time than the one which is already there, we merge.. drop the current one
                stack.pop()
        return len(stack)  
