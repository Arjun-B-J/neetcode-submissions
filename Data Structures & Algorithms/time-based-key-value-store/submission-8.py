class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Using a tuple (timestamp, value) uses slightly less memory than a list
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # If the key doesn't exist, return empty string immediately
        values = self.store.get(key, [])
        
        res = ""
        l, r = 0, len(values) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if values[mid][0] <= timestamp:
                # This is a valid candidate! Record it.
                res = values[mid][1]
                # Keep searching to the right for a more recent valid timestamp
                l = mid + 1
            else:
                # Timestamp is too large, we must search the left half
                r = mid - 1
                
        return res