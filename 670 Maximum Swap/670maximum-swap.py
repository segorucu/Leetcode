class Solution:
    def maximumSwap(self, num: int) -> int:
        
        if num == 0:
            return 0

        arr = []
        while num:
            arr.append(num%10)
            num = num // 10
        
        for baseind in range(len(arr)-1,0,-1):
            ind =  arr.index(max(arr[0:baseind]))
            if arr[ind] > arr[baseind]:
                arr[ind], arr[baseind] = arr[baseind], arr[ind]
                break

        arr.reverse()
        sm = 0 
        for i in range(len(arr)):
            sm = sm * 10 + arr[i]

        return sm