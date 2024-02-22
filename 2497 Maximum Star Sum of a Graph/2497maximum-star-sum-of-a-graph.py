class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        
        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(vals[b])
            graph[b].append(vals[a])
        # for i, val in enumerate(vals):
        #     graph[i].append(val)

        ans = max(vals)
        for key,values in graph.items():
            sm = vals[key]
            values.sort(reverse=True)
            count = min(k,len(values))
            for i in range(count):
                if values[i] < 0:
                    break
                sm += values[i]
            ans = max(ans,sm)



        return ans