class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr = sorted(arr)
        n = len(arr)
        beg = n // 20
        mean = 0.
        for i in range(beg,n-beg):  
            mean += arr[i]
        mean /= (n-2*beg)
        return mean      