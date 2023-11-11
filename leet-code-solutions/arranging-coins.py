class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 1, n
        res = 1
        while low <= high:
            mid = (low + high) // 2
            coins = (mid / 2) * (mid + 1)
            
            if coins > n:
                high = mid - 1
            else:
                low = mid + 1
                res = max(res, mid)    

        return res        