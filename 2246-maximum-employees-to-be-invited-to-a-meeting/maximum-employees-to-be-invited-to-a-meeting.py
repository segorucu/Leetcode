class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        

        max_cycle = 0
        n = len(favorite)
        visited = set()
        for i in range(n):
            if i in visited:
                continue

            stack = []
            current = i
            while current not in visited:
                visited.add(current)
                stack.append(current)
                current = favorite[current]
            if current in stack:
                max_cycle = max(max_cycle, len(stack) - stack.index(current) )

        inverse =collections.defaultdict(list)
        for i,val in enumerate(favorite):
            inverse[val].append(i)

        def dfs(node,banned):
            depth = 0
            for nei in inverse[node]:
                if nei != banned:
                    depth = max(depth,dfs(nei,banned))
            return depth + 1

        pairs = []
        for i in range(n):
            if favorite[favorite[i]] == i and i < favorite[i]:
                pairs.append([i,favorite[i]])

        pair_length = 0
        for a,b in pairs:
            one = dfs(a,b)
            two = dfs(b,a)
            pair_length += one + two


        return max(max_cycle,pair_length)


