class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        visited = set()
        ans = []
        prev = 0
        for a,b in zip(A,B):
            if a in visited:
                prev += 1
            visited.add(a)
            if b in visited:
                prev += 1
            visited.add(b)
            ans.append(prev)
        return ans
