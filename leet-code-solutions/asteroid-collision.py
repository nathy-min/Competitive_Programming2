class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        n = len(asteroids)
        for i in range(1, n):
            if asteroids[i] < 0:
                temp = 0
                while stack and stack[-1] > 0 and stack[-1] <= abs(asteroids[i]):
                    temp = stack[-1]
                    stack.pop()
                    if abs(asteroids[i]) == temp:
                        break   
                if not stack or stack[-1] < 0:
                    if abs(asteroids[i]) != temp:
                        stack.append(asteroids[i])    
            else:
                stack.append(asteroids[i])

        return stack        
