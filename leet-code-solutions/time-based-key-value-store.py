class TimeMap:

    def __init__(self):
        self.structure = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.structure:
            self.structure[key] = []
        self.structure[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        temp = self.structure.get(key, [])

        low, high = 0, len(temp) - 1
        while low <= high:
            mid = (low + high) // 2

            if temp[mid][1] <= timestamp:
                ans = temp[mid][0]
                low = mid + 1
            else:
                high = mid - 1
        return ans