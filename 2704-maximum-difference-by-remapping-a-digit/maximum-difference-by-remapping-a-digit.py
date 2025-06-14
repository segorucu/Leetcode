class Solution:
    def minMaxDifference(self, num: int) -> int:
        
        arr = []
        while num:
            arr.append(num % 10)
            num = num // 10

        arr.reverse()
        n = len(arr)
        d1 = 9
        i = 0
        while i < n:
            if arr[i] < 9:
                d1 = arr[i]
                break
            i += 1

        def calcnum(arr):
            arr.reverse()
            mult = 1
            curr = 0
            for i in range(n):
                curr += arr[i] * mult
                mult *= 10
            return curr

        def findmax(arr):
            for i in range(n):
                if arr[i] == d1:
                    arr[i] = 9

            return calcnum(arr)

        def findmin(arr):
            d1 = arr[0]
            for i in range(n):
                if arr[i] == d1:
                    arr[i] = 0

            return calcnum(arr)

            

        maxval = findmax(arr[:])
        minval = findmin(arr[:])

        return maxval - minval