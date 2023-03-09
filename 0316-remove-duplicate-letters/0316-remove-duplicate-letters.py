class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        
        for char in s:
            if char in stack:
                count[char] -= 1
                continue
            while len(stack) > 0 and stack[-1] > char and count[stack[-1]] > 0:
                stack.pop()
            count[char] -= 1
            stack.append(char) 
            
        return "".join(stack)