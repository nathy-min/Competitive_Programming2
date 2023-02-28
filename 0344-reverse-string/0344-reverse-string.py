
class Solution:
    def reverser(self,s, ptr):
        if ptr  == len(s)//2:
            # s[ptr], s[~ptr] = s[~ptr], s[ptr]
            # print(s[ptr])
            # print(s[~ptr])
            return
        s[ptr], s[~ptr] = s[~ptr], s[ptr]
        self.reverser(s, ptr +  1)
        return
        
    
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ptr = 0
        print(len(s))

        self.reverser(s,ptr)
        