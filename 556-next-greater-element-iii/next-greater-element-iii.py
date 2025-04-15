class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        maxval = 2147483647
        arr = list(str(n))
        m = len(arr)
        for l in range(m-1,-1, -1):
            for r in range(m-1, l, -1):
                if arr[l] < arr[r]:
                    arr[r], arr[l] = arr[l], arr[r]
                    arr = arr[0:l+1] + sorted(arr[l+1:])
                    val = int("".join(arr))
                    # print(val)
                    # print(maxval)
                    if val > maxval:
                        return -1
                    return val

        return -1