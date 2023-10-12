class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dx, dy = 0, 1
        x, y = 0, 0

        for d in instructions:
            if d == 'G':
                x, y = x + dx, y + dy
            elif d == 'L':
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx 

        return (x, y) == (0, 0) or (dx, dy) != (0, 1)