class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            val = i
            count = 0
            while val != 0:
                count += (val % 2)
                val = val>>1
            res.append(count) 
        
        return res