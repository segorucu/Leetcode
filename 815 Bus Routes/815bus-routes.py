from collections import defaultdict, deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        for i, route in enumerate(routes):
            routes[i] = sorted(route)

        def isthereaconnection(routi,routj):
            pi = pj = 0
            while pi < len(routi) and pj < len(routj):
                vi, vj = routi[pi], routj[pj]
                if vi == vj:
                    return True
                if vi < vj:
                    pi += 1
                else:
                    pj += 1
            return False

        bustobus = defaultdict(list)
        n= len(routes)
        for i in range(n):
            for j in range(i+1,n):
                if isthereaconnection(routes[i],routes[j]):
                    bustobus[i].append(j)
                    bustobus[j].append(i)

        targetbus = set()
        queue = deque()
        for i,route in enumerate(routes):
            if target in route:
                targetbus.add(i)
            if source in route:
                queue.append((1,i))

        visited = set()
        while queue:
            cost, node = queue.popleft()
            visited.add(node)
            if node in targetbus:
                return cost
            for neigh in bustobus[node]:
                if neigh not in visited:
                    queue.append((cost+1,neigh))


        return -1


        