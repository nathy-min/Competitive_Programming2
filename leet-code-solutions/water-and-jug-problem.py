class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:   
        j1 = jug1Capacity
        j2 = jug2Capacity
        seen = set()

        def dfs(num):
            if num == targetCapacity:
                return True
            if num < 0 or num > j1 + j2:
                return False
            if num in seen:
                return False
            seen.add(num)
                
            return dfs(num + j1) or dfs(num - j1) or dfs(num + j2) or dfs(num - j2)

        return dfs(0)          

