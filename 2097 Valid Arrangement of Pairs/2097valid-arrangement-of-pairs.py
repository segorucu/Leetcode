class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        
        outDegree = collections.defaultdict(int)
        inDegree = collections.defaultdict(int)
        startswith = collections.defaultdict(collections.deque)
        for start, end in pairs:
            startswith[start].append(end)
            outDegree[start] += 1
            inDegree[end] += 1

        for key,val in outDegree.items():
            if val - inDegree[key] == 1:
                start = key
                break
        else:
            start = pairs[0][0]
        
        nodeStack = [start]
        result = []

        while nodeStack:
            node = nodeStack[-1]
            if startswith[node]:
                nextnode = startswith[node].popleft()
                nodeStack.append(nextnode)
            else:
                result.append(node)
                nodeStack.pop()

        result = list(reversed(result))
        ans = []
        for i in range(1,len(result)):
            start, end = result[i-1], result[i]
            ans.append([start,end])

        return ans
