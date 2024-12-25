from sortedcontainers import SortedList
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        m = len(queries)
        new_queries = []
        for i in range(m):
            q = queries[i]
            new_queries.append([min(q),max(q),i])
        new_queries.sort(key=lambda x: -x[1])
        
        ans = m * [None]
        stack = [(-float("inf"),-1)]
        i = n-1
        
        for q in new_queries:
            x, y, ans_ind = q
            if x == y or heights[y] > heights[x]:
                ans[ans_ind] = y
                continue
            minval = heights[x]+1
            while i > y:
                while heights[i] >= -stack[-1][0]:
                    stack.pop()
                stack.append((-heights[i],i))
                i -= 1
            k = bisect.bisect_left(stack, (-minval,))
            if k == len(stack) or -stack[k][0] < minval:
                k -= 1
            ind = stack[k][1]
            ans[ans_ind] = ind
        return ans