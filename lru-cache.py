class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.q = deque()
        self.dic = {}

    def get(self, key: int) -> int:
        if key in self.dic:
            self.q.remove(key)
            self.q.append(key)   
            return self.dic[key]
        return -1      

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key] = value
            self.q.remove(key)
            self.q.append(key)
            return

        if len(self.q) == self.capacity:
            k = self.q.popleft()
            del self.dic[k]
        self.q.append(key)
        self.dic[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)