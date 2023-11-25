class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoded = encoding
        

    def next(self, n: int) -> int:
        while self.encoded:
            if self.encoded[0] >= n:
                self.encoded[0] -= n
                return self.encoded[1]
            n -= self.encoded[0]
            self.encoded.pop(0)
            self.encoded.pop(0)    
        return -1        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)