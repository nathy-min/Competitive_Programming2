class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_d = (hour % 12) * 30 + minutes * 0.5
        min_d = minutes * 6
        ans  = abs(hour_d - min_d) 
        if ans > 180:
            return 360 - ans
        return ans     