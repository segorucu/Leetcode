class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        recipeset = set(recipes)
        supplies = set(supplies)
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        required = collections.defaultdict(list)
        n = len(recipes)
        for i,recipe in enumerate(recipes):
            indegree[recipe] = 0
            required[recipe] = ingredients[i]

        for i,recipe in enumerate(recipes):
            for j, ing in enumerate(ingredients[i]):
                if ing in recipeset and ing not in supplies:
                    indegree[recipe] += 1
                    graph[ing].append(recipe)

        res = set()
        queue = deque()
        for k,v in indegree.items():
            if v == 0:
                queue.append(k)

        while queue:
            curr = queue.popleft()
            for supply in required[curr]:
                if supply not in supplies:
                    break
            else:
                supplies.add(curr)
                del indegree[curr]
                del required[curr]
                for neigh in graph[curr]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        queue.append(neigh)
                del graph[curr]
                res.add(curr)

    
        return list(res)
