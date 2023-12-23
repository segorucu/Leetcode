class Solution:
    def isPathCrossing(self, path: str) -> bool:

        tab = {"N": (0,1), "E": (1,0), "S": (0,-1), "W": (-1,0)}

        curr = (0,0)
        visited = set()
        visited.add(curr)
        for c in path:
            curr = (curr[0]+tab[c][0],curr[1]+tab[c][1])
            if curr in visited:
                return True
            visited.add(curr)

        return False
        