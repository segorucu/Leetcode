class Solution:
    def getPermutation(self, n: int, k: int) -> str:


        def backtrack(count,curr):
            
            if len(curr) == n:
                count += 1
                if count == k:
                    return (curr, count)
                else:
                    return (None, count)

            for j in range(n):
                if str(j+1) in curr:
                    continue
                curr += str(j+1)
                (res, count) = backtrack(count,curr)
                if res is not None:
                    return res, count
                curr = curr[:-1]
            return None, count


        return backtrack(0,"")[0]

        