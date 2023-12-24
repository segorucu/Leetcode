class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = (10**9 + 7)
        def helper(arr,edge):

            arr.extend([1,edge])
            arr.sort()
            sides = set()
            for i in range(len(arr)):
                for j in range(i+1,len(arr)):
                    sides.add(arr[j]-arr[i])
            return sides

        X = helper(hFences,m)
        Y = helper(vFences,n)
        
        o = X & Y
        if len(o) == 0:
            return -1
        return (max(o) ** 2) % MOD
        