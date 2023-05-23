class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x): 
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        parent = {}
        def union(c1, c2):
            pc1 = find(c1)
            pc2 = find(c2)
            if pc1 == pc2:
                return
            parent[pc2] = pc1    
        
        for eq in equations:
            parent[eq[0]] = eq[0]
            parent[eq[3]] = eq[3]
            
        for eq in equations: 
            if eq[1] == '=':
                x, y = eq[0], eq[3]
                union(x, y)
        
        for eq in equations:
            if eq[1] == '!':
                if find(eq[0]) == find(eq[3]):
                    return False
        return True