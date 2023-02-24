class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = {}
        stack = []
        for i in range(len(position)):
            pair[position[i]] = speed[i]
        pair = dict(sorted(pair.items())[::-1])
        for k,v in pair.items():
            time = (target - k)/v
            if stack:
                
                if time > stack[-1]:
                    stack.append(time)
            else:
                stack.append(time)
        print(pair)
        return len(stack)        