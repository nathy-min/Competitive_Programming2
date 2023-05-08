class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        inbound = [0 for _ in range(len(recipes))]
        supplies = set(supplies)
        
        for i in range(len(recipes)):
            for ing in ingredients[i]:
                if ing in supplies:
                    continue
                graph[ing].append((recipes[i], i))
                inbound[i] += 1
        
        q = deque()
        for i in range(len(recipes)):
            if inbound[i] == 0:
                q.append(recipes[i])
        
        ans = []
        recipes = set(recipes)
        while q:
            ing = q.popleft()
            if ing not in recipes:
                continue
            ans.append(ing)
            for rec in graph[ing]:
                inbound[rec[1]] -= 1
                if inbound[rec[1]] == 0:
                    q.append(rec[0])
        
        return ans