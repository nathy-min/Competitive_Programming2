# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def search(low, high, flag):
            while low <= high:
                m = (low + high) // 2
                temp = mountain_arr.get(m)
                if temp == target:
                    return m
                if temp > target:
                    if not flag:
                        high = m - 1
                    else:
                        low = m + 1    
                else:
                    if not flag:
                        low = m + 1
                    else:
                        high = m - 1    
            return -1            

        l = 0
        r = mountain_arr.length() - 1
        maxnum_idx = 0
        while l <= r:
            m = (l + r) // 2
            temp = mountain_arr.get(m)
            maxnum_idx = m if temp > mountain_arr.get(maxnum_idx) else maxnum_idx

            if temp < mountain_arr.get(m + 1):
                l = m + 1
            else:
                r = m - 1

        target1 = search(0, maxnum_idx, 0)
        target2 = search(maxnum_idx + 1, mountain_arr.length() - 1, 1)
        print(maxnum_idx)
        return target1 if target1 != -1 else target2        

                
