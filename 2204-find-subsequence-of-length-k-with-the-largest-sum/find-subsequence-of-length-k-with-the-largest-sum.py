class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        arr = []
        for i,val in enumerate(nums):
            arr.append((val,i))

        arr.sort(reverse=True)
        arr = arr[0:k]
        arr.sort(key = lambda x:x[1])
        ans = []
        for val in arr:
            ans.append(val[0])

        return ans