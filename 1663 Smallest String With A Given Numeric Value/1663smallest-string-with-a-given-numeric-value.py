class Solution:
    def getSmallestString(self, n: int, k: int) -> str:

        base = 96
        letters = 26
        arr = [97] * n
        k -= n
        for i in range(n-1,-1,-1):
            diff = min(25,k)
            arr[i] += diff
            k -= diff
            if k == 0:
                break

        ans = ""
        for i in range(n):
            ans += chr(arr[i])


        return ans