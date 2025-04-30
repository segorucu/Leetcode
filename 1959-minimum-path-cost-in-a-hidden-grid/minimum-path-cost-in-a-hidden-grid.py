# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> int:
#        
#
#    def isTarget(self) -> bool:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        visited = set()
        costgraph = collections.defaultdict(int)
        directions = {
                      'U': (-1,0), 
                      'D': (1,0),
                      'L': (0,-1),
                      'R': (0,1)
                      }

        parentdir = {"U": "D", "D": "U", "L": "R", "R": "L"}

        self.target = None
        def dfs(parent,r,c):
            if master.isTarget():
                self.target = (r,c)

            for move in directions.keys():
                nr = r + directions[move][0]
                nc = c + directions[move][1]
                if master.canMove(move) and (nr,nc) not in visited:
                    cost = master.move(move)
                    visited.add((nr,nc))
                    costgraph[(nr,nc)] = cost
                    dfs(parentdir[move],nr,nc)

            master.move(parent)
        
        visited.add((0,0))
        dfs(None,0,0)
        # print(costgraph)
        if self.target not in costgraph:
            return -1

        hp = []
        heappush(hp, (0,0,0)) #cost,r,c
        visited = set()
        totalcost = defaultdict(int)
        totalcost[(0,0)] = 0
        while hp:
            cost, r, c = heappop(hp)
            visited.add((r,c))
            for move,(dr,dc) in directions.items():
                nr, nc = r+dr, c+dc
                if (nr,nc) in costgraph and (nr,nc) not in visited:
                    add = costgraph[(nr,nc)]
                    newcost = cost + add
                    if (nr,nc) not in totalcost or newcost < totalcost[(nr,nc)]:
                        totalcost[(nr,nc)] = newcost
                        heappush(hp,(newcost,nr,nc))

        return totalcost[self.target]

        # visited = {(1,0),}
        # costgraph: (1,0): 1

        # dfs(None,0,0):
        # r1 = 0
        # c1 = 1
        # nr = 1
        # nc = 0
        # nr1 = 1
        # nc1 = 1

        # dfs(U,1,0):
        # r1 = 1
        # c1 = 1

        
