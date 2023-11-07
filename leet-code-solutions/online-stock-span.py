class StockSpanner:

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        if not self.stock:
            self.stock.append((price, 0))
            return 1
        
        count = 1
        while self.stock and price >= self.stock[-1][0]:
            count += self.stock[-1][1] + 1
            self.stock.pop()

        self.stock.append((price, count - 1))
        return count       


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)