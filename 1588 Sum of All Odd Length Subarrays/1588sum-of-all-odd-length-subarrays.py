class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        n = len(arr)
        ans = 0
        for i in range(n):
            curr = 0
            count = 0
            for j in range(i,n):
                count += 1
                curr += arr[j]
                if count % 2 == 1:
                    ans += curr

        return ans
