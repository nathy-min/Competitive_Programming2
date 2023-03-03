class Solution:
    def checker(self, mid):
        day = 0
        left = right = 0
        while right < len(self.weights):
            if (self.weights[right] - left) == mid:
                day += 1
                left = self.weights[right]
                right += 1
            elif self.weights[right] -left > mid:
                day += 1
                left = self.weights[right - 1]
                right += 1
            else:
                right += 1
        
        if self.weights[right - 1] != left:
            day += 1
            
        return day <= self.days
        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        self.weights = weights
        self.days = days
        best_days = 0 
        
        for i in range(1, len(weights)):
            self.weights[i] += self.weights[i - 1]
            
        while low <= high:
            mid = (low + high) // 2
            if self.checker(mid):
                best_days = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return best_days       
            
            