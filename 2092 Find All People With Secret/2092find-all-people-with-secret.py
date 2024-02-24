class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key =  lambda x:x[2])
        
        
        knowset = set()
        knowset.add(0)
        knowset.add(firstPerson)
        r = 0
        n = len(meetings)
        while r < n:
            connections = collections.defaultdict(list)
            x, y, time = meetings[r]
            connections[x].append(y)
            connections[y].append(x)
            while r+1 < n and time == meetings[r+1][2]:
                r += 1
                x, y, _ = meetings[r]
                connections[x].append(y)
                connections[y].append(x)
            anybodyknows = False
            queue = collections.deque()
            for x in connections.keys():
                if x in knowset:
                    queue.append(x)
                    knowset.add(x)
            while queue:
                node = queue.popleft()
                for neigh in connections[node]:
                    if neigh not in knowset:
                        queue.append(neigh)
                        knowset.add(neigh)
            r += 1  

        
        ans = list(knowset)
        return ans
        