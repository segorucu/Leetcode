class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        
        n = len(groups)
        assigned = n * [-1]


        graph = collections.defaultdict(list)
        for i,a in enumerate(groups):
            graph[a].append(i)

        maxval = max(groups)
        visited = set()
        for i,element in enumerate(elements):
            if element in visited:
                continue
            visited.add(element)
            curtot = element
            while curtot <= maxval:
                for ind in graph[curtot]:
                    if assigned[ind] == -1:
                        assigned[ind] = i
                curtot += element


        return assigned