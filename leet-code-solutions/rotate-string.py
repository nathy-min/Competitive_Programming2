class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        for i in range(len(s)):
            j = 0
            while j < len(goal) and s[(i + j) % len(s)] == goal[j]:
                j += 1

            if j == len(goal):
                return True   

        return False        