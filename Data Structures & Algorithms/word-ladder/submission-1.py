class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList: #trick to build the adjaceny list since word len is smaller
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                nei[pattern].append(word)
        
        q=deque()
        q.append(beginWord)
        visit = set()
        visit.add(beginWord)
        #do bfs to find the shortest path
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j]+"*"+word[j+1:]
                    for neighbour in nei[pattern]:
                        if not neighbour in visit:
                            visit.add(neighbour)
                            q.append(neighbour) 
            res+=1
        return 0