class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 1:
            return
        val = s.pop()
        self.reverseString(s)
        s.insert(0, val)
        return 
        