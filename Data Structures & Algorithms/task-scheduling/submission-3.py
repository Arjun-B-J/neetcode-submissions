class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque() #for putting in buffered stuff picked from heap with n timeout, we pick it back up when the timer exceeds
        time = 0
        while maxHeap or q:
            time+=1
            if maxHeap:
                count = 1+ heapq.heappop(maxHeap) # here since vals are neg , inc will decrease abs(negval)
                if count: #if count, then we timeout by adding it to the q
                    q.append((count,time+n)) #no need to neg count here, since is already handled my heap
            if q:
                if q[0][1]<=time:
                    heapq.heappush(maxHeap,q.popleft()[0]) #if the first ele in q is having time less than our time, the timeout is done , we pop and add it back to heap
        return time
                