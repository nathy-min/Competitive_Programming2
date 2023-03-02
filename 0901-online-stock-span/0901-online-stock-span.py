class StockSpanner:

    def __init__(self):
        self.stack = []  

    def next(self, price: int) -> int:
        temp = 0
        while self.stack and price >= self.stack[-1][1]:
            temp += (self.stack[-1][0] + 1)
            self.stack.pop()
        
        self.stack.append((temp, price))
        return temp + 1
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)