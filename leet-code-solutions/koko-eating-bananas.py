class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            m = l + (r - l) // 2
            curr_hours = 0
            for pile in piles:
                curr_hours += ceil(pile / m)
            
            if curr_hours <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1

        return res                