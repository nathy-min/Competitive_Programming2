class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dic = defaultdict(int)
        for i in range(len(edges)):
            dic[edges[i][0]] += 1
            dic[edges[i][1]] += 1
        
        return max(dic, key=lambda key: dic[key])