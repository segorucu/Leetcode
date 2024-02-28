class Solution:
    def numSplits(self, s: str) -> int:

        n = len(s)
        left = [0 for _ in range(n)]
        visited = set()
        for i,a in enumerate(s):
            visited.add(a)
            left[i] = len(visited)
        
        right = [0 for _ in range(n)]
        visited = set()
        for i in range(n-1,-1,-1):
            visited.add(s[i])
            right[i] = len(visited)

        sm = 0
        for i in range(n-1):
            if left[i] == right[i+1]:
                sm += 1


        return sm
