class Solution:
    def maxLength(self, arr: List[str]) -> int:

        new = []
        n = len(arr)
        for i in range(n):
            visited = set()
            for a in arr[i]:
                if a in visited:
                    break
                visited.add(a)
            else:
                new.append(arr[i])
        arr = new.copy()
        del new
        n = len(arr)
        
        visited = set()
        def backtrack(i,visited):
            if i == n:
                return len(visited)

            for a in arr[i]:
                if a in visited:
                    res = backtrack(i+1,visited)
                    break
            else:
                visited.update(arr[i])
                one = backtrack(i+1,visited)
                visited -= set(arr[i])
                two = backtrack(i+1,visited)
                res = max(one,two)
            return res
        

        return backtrack(0,visited)