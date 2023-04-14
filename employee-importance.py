"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def dfs(self, id):
        
        self.T_importance += self.emp[id]
        
        for ids in self.sub[id]:
            self.dfs(ids)
        
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.emp = {}
        self.sub = {}
        self.T_importance = 0
        
        for em in employees:
            self.emp[em.id] = em.importance
            self.sub[em.id] = em.subordinates
        
        self.dfs(id)
        
        return self.T_importance