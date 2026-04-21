class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            l,r = 0,len(self.store[key])-1
            while(l<=r):
                mid = (l+r)//2
                if self.store[key][mid][0] == timestamp:
                    return self.store[key][mid][1]
                if timestamp > self.store[key][mid][0]:
                    l=mid+1
                else:
                    r=mid-1
            print(mid,l,r,timestamp)
            if r<0:
                r=0
            if self.store[key][r][0]>timestamp:
                return ""
            return self.store[key][r][1]

        return ""
