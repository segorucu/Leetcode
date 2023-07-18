from collections import defaultdict
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equal = defaultdict(list)
        notequal = defaultdict(list)
        valtab = defaultdict(int)

        for eq in equations:
            var1 = eq[0]
            sign = eq[1:3]
            var2 = eq[3]
            if sign == "==":
                equal[var1].append(var2)
                equal[var2].append(var1)
            else:
                if var1 == var2:
                    return False
                notequal[var1].append(var2)
                notequal[var2].append(var1)

        def dfs(node):
            visited.add(node)
            for neigh in equal[node]:
                if neigh not in visited:
                    dfs(neigh)

        island = 0
        for key in equal:
            visited =set()
            if key not in valtab:
                island += 1
                dfs(key)
                visited = list(visited)
                for node in visited:
                    valtab[node] = island

        for key in notequal:
            for neigh in notequal[key]:
                if key in valtab and neigh in valtab:
                    if valtab[key] == valtab[neigh]:
                        return False

        return True

