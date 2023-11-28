class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        options = "abc"
        ans = []
        def backtrack(string):
            if len(string) == n:
                ans.append(string)
                return
            if len(ans) == k:
                return

            for c in options:
                if string and c == string[-1]:
                    continue
                string += c
                backtrack(string)
                string = string[0:-1]
                if len(ans) == k:
                    return

        backtrack("")
        if len(ans) < k:
            return ""
        else:
            return ans[k-1]

        