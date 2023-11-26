class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        if k > n:
            return ans


        def backtrack(start,sm,curr):
            if len(curr) == k:
                if sm == n:
                    ans.append(curr[:])
                return

            if sm > n:
                return

            for i in range(start,10):
                curr.append(i)
                backtrack(i+1,sm+i,curr)
                curr.pop()


        backtrack(1,0,[])
        return ans
        