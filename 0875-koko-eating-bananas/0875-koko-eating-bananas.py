class Solution:
        
        
    def isValid(self, k, piles, h):
        hoursTaken = 0
        
        for pile in piles:
            hoursTaken += ceil(pile/k) 
            if hoursTaken > h: 
                return False

        return True
    
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        minimumSpeed = 1
        
        while start <= end:
            mid = start + (end - start) // 2
            if self.isValid(mid, piles, h):
                minimumSpeed = mid
                end = mid - 1
            else: 
                start = mid + 1
        
        
        return minimumSpeed
                
                