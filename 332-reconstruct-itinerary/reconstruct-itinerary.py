class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        

        graph = defaultdict(lambda: SortedList())
        # timer = defaultdict(int)
        for departure, arrival in tickets:
            graph[departure].add(arrival)
            # timer[departure] = 0
        # print(graph)
        
        ans = ["JFK"]
        def dfs(loc):
            if len(ans) == len(tickets) + 1:
                return True
            if len(graph[loc]) == 0:
                return False

            destinations = graph[loc]
            for i,dest in enumerate(destinations):
                graph[loc].pop(i)
                ans.append(dest)
                if dfs(dest): return True
                graph[loc].add(dest)
                ans.pop()

            return False


        dfs("JFK")
        return ans