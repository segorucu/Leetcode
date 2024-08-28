class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        

        n= len(arr)
        for l in range(n-1,-1,-1):
            selectedr = -1
            rval = -1
            for r in range(l,n):
                if arr[l] > arr[r] and arr[r] != rval:
                    selectedr = r
                    rval = arr[r]
                    # print(selectedr, rval)
            if selectedr > -1:
                arr[l], arr[selectedr] = arr[selectedr], arr[l]
                return arr
        return arr
