# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        high = n
        low = 1
        while low <= high:
            mid = (low + high) // 2
            if low == high :
                return low
            
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                else:
                    high = mid - 1
            elif not isBadVersion(mid):
                low = mid + 1
                
             