class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        

        graph = collections.defaultdict(list)
        children = set()
        for region in regions:
            parent = region[0]
            for i in range(1, len(region)):
                graph[parent].append(region[i])
                children.add(region[i])

        parentlist = []
        for key in graph.keys():
            if key not in children:
                parentlist.append(key)

        def dfs(node):
            
            reg1, reg2 = False, False

            if node == region1:
                reg1 = True
            elif node == region2:
                reg2 = True

            for child in graph[node]:
                one, two, name = dfs(child)
                if one and two:
                    return one, two, name
                reg1 = reg1 or one
                reg2 = reg2 or two
            
            if reg1 and reg2:
                return True, True, node
            else:
                return reg1, reg2, ""
                
        return dfs(parentlist[0])[2]
