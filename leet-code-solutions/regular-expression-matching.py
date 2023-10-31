class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def rec(s_index, p_index):
            if (s_index, p_index) in cache: 
                return cache[(s_index, p_index)]
            
            if s_index >= len(s) and p_index >= len(p): 
                cache[(s_index, p_index)] = True
                return cache[(s_index, p_index)]
            
            if p_index >= len(p): 
                cache[(s_index, p_index)] = False
                return cache[(s_index, p_index)]
            
            match = (s_index < len(s) and p[p_index] in {s[s_index], '.'} )
            
            if p_index + 1 <len(p) and p[p_index +1] == '*':                
                cache[s_index, p_index] = rec(s_index, p_index + 2) or (match and rec(s_index + 1, p_index))               
                return cache[s_index, p_index]
            
            if match:
                cache[s_index, p_index] = rec(s_index + 1, p_index+1)
                return cache[s_index, p_index]
            
            cache[s_index, p_index] = False
            return cache[s_index, p_index]
        
        return rec(0, 0)