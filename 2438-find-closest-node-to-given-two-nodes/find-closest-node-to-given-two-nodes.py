class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        if node1 == node2:
            return node1
        
        def traverse(node):
            distance= 0
            graph = {}
            while node != -1:
                if node in graph:
                    return graph
                graph[node] = distance
                node = edges[node]
                distance += 1
            return graph

        graph1 = traverse(node1)
        graph2 = traverse(node2)

        common = graph1.keys() & graph2.keys()
        if not common:
            return -1

        maxdist = float("inf")
        selected = 10**6
        for key in common:
            dist = max(graph1[key], graph2[key])
            if dist < maxdist:
                maxdist = dist
                selected = key
            elif dist == maxdist:
                selected = min(selected, key)

        return selected