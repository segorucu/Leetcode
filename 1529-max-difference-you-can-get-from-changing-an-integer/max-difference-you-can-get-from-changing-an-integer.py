class Solution:
    def maxDiff(self, num: int) -> int:
        
        arr = []
        while num:
            arr.append(num % 10)
            num = num // 10

        arr.reverse()

        def converttonum(arr):

            mult = 1
            curr = 0
            for i in range(len(arr)):
                curr += mult * arr[i]
                mult *= 10
            return curr
                

        def findmax(arr):
            n= len(arr)
            for i in range(n):
                if arr[i] < 9:
                    x = arr[i]
                    break
            else:
                arr.reverse()
                return converttonum(arr)

            for i in range(n):
                if arr[i] == x:
                    arr[i] = 9
            
            arr.reverse()
            return converttonum(arr)

        def findmin(arr):
            n = len(arr)
            for i in range(n):
                if arr[i] > 1:
                    x = arr[i]
                    break
            else:
                arr.reverse()
                return converttonum(arr)

            if arr[0] == x:
                y = 1
            else:
                y = 0

            for i in range(n):
                if arr[i] == x:
                    arr[i] = y
            arr.reverse()
            return converttonum(arr)


        a = findmax(arr[:])
        b = findmin(arr[:])

        return a-b
