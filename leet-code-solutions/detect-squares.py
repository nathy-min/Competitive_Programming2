class DetectSquares:

    def __init__(self):
        self.dic = defaultdict(int)
        self.lst = []

    def add(self, point: List[int]) -> None:
        self.dic[tuple(point)] += 1
        self.lst.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        xq, yq = point
        for x, y in self.lst:
            if   (abs(xq - x) != abs(yq - y)) or x == xq or y == yq:
                continue
            print(self.dic[(x, yq)], self.dic[(y, xq)])    
            res += self.dic[(x, yq)] * self.dic[(xq, y)] 
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)