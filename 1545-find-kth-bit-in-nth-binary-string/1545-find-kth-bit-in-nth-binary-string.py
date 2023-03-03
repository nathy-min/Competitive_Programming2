class Solution:
    def kthbit(self, n):
        if n == 1:
            return "0"
        if n == 2:
            return "011"
        
        prev = self.kthbit(n - 1)
        inverted = prev[:len(prev)//2] + "0" + prev[(len(prev) // 2) + 1:]
        curr = prev + "1" + inverted
        return curr
        
    def findKthBit(self, n: int, k: int) -> str:
        
        return self.kthbit(n)[k - 1]
        