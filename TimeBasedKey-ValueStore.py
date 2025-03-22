from collections import defaultdict
from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key][timestamp] = value
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        time = self.timeMap[key]
        print(time)
        idx = time.bisect_right(timestamp)-1
        print(idx)

        if idx >= 0 :
            closest_time = time.iloc[idx]
            return time[closest_time]
        
timeMap = TimeMap()

timeMap.set("alice", "happy", 1)
print(timeMap.get("alice", 1))    
timeMap.set("alice", "hy", 2)  
print(timeMap.get("alice", 2))   

