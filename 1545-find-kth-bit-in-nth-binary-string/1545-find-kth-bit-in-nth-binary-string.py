class Solution:  
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        if k == 2**(n - 1):
            return "1"
        if k < 2**(n - 1):
            return self.findKthBit(n - 1, k)
        elif k - 2**(n - 1) == 2**(n - 2):
            return str(1 - int(self.findKthBit(n - 1, k - 2**(n - 1)))) 
        else:
            return str(self.findKthBit(n - 1, k - 2**(n - 1)))
        
        