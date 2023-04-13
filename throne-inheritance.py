class ThroneInheritance:
    def dfs(self, name):
        if not name:
            return []
        ans = []
        if not self.dead[name]:
            ans.append(name)

        for names in self.kingdom[name]:
            ans.extend(self.dfs(names))

        return ans            

    def __init__(self, kingName: str):
        self.kingdom = defaultdict(list)
        self.dead = defaultdict(int)
        self.kingname = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.kingdom[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead[name] = 1

    def getInheritanceOrder(self) -> List[str]:
        return self.dfs(self.kingname)


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()