from functools import reduce
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:

        
        arr = [0] + [int(c) for c in str(n)]
        tot = sum(arr)
        i = len(arr)-1
        add = 0
        mult = 0
        while tot > target:
            dum = arr[i]
            tot = tot - arr[i] + 1
            arr[i] = 0
            arr[i-1] += 1
            i -= 1
            add += (10-dum) * 10**mult
            mult += 1

        return add