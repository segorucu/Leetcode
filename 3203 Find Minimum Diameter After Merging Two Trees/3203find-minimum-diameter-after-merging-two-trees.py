class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:


        def build_edges(edges):
            adj = collections.defaultdict(list)
            for a,b in edges:
                adj[a].append(b)
                adj[b].append(a)
            return adj

        adj1 = build_edges(edges1)
        adj2 = build_edges(edges2)

        def get_diameter(cur, par, adj):
            max_d = 0
            max_paths = [0,0]
            for nei in adj[cur]:
                if nei == par: 
                    continue
                dia, depth = get_diameter(nei, cur, adj)
                max_d = max(max_d, dia)
                heappush(max_paths, depth)
                heappop(max_paths)
            max_d = max(max_d, sum(max_paths))
            return max_d, 1+max(max_paths)

        d1, _ = get_diameter(0, -1, adj1)
        d2, _ = get_diameter(0, -1, adj2)

        return max(d1, d2, (d1+1)//2 + (d2+1)//2 + 1 )

        