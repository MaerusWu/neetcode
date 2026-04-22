class TimeMap:

    def __init__(self):
        self.keyStore =  defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.keyStore:
            return ""
        l, r, res = 0, len(self.keyStore[key]) - 1, ""
        while l < r:
            mid = l + (r - l)//2 
            if self.keyStore[key][mid][0] <= timestamp:
                res = self.keyStore[key][mid][1]
                l = mid + 1
            else:
                r = mid
        if self.keyStore[key][l][0] <= timestamp:
            res = self.keyStore[key][l][1] 
        return res

            

