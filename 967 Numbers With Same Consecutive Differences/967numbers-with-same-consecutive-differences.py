class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        def convert(curr):
            num = ''.join(str(e) for e in curr)
            num = int(num)
            return num

        ans = []
        def backtrack(curr):
            if len(curr) == n:
                num =convert(curr)
                ans.append(num)
                return
            elif len(curr) > n:
                return

            i = curr[-1]
            if i + k < 10:
                curr.append(i+k)
                backtrack(curr)
                curr.pop()
            i = curr[-1]
            if i - k >= 0 and k != 0:
                curr.append(i-k)
                backtrack(curr)
                curr.pop()
                

        for i in range(1,10):
            backtrack([i])

        return ans