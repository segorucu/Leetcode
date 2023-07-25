class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        right = n-1
        while True:
            i = (left+right) // 2
            if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
                return i
            elif arr[i] > arr[i-1]:
                left = i+1
            else:
                right = i
            