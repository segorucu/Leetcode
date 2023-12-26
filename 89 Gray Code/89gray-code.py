class Solution:
    def grayCode(self, n: int) -> List[int]:

        def recurse(n):
            if n == 1:
                return ["0","1"]

            left = recurse(n-1)
            right = list(reversed(left))
            tot = left + right
            for i,a in enumerate(tot):
                if i < len(tot) / 2:
                    tot[i] = "0" + a
                else:
                    tot[i] = "1" + a
            return tot

        arr = recurse(n)
        for i,a in enumerate(arr):
            arr[i] = int(a,2)

        return arr
        