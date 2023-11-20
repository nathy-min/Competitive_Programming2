class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        a_max = 0
        stack = []
        
        for i in range(len(heights)):
            temp = (i,i)
            while stack and heights[stack[-1][0]] > heights[i]:
                tem = heights[stack[-1][0]] * (i - stack[-1][1])
                a_max = max(a_max, tem)
                temp = stack.pop()
            stack.append((i, temp[1]))
        
        return a_max