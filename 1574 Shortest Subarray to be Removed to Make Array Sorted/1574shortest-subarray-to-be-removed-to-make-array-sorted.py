from bisect import bisect_right, bisect
from sortedcontainers import SortedList
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        # 1,2,3,10,4,2,3,5
        # 0,0,0,0 ,1,2,

        n = len(arr)
        dp = n * [0]
        for i in range(1,n):
            if arr[i] < arr[i-1]:
                ans = n-i
                beg = i
                break
        else:
            return 0


        stack = []
        for i, val in enumerate(arr):
            if not stack or val >= stack[-1][0]:
                stack.append((val,i))
            else:
                break

        print(stack)
        r = n-1
        while r >= beg:
            l = bisect_left(stack,(arr[r],))
            while l+1 < len(stack) and stack[l][0] == stack[l+1][0] and stack[l][0] == arr[r]:
                l += 1
            if stack and l < len(stack) and stack[l][1] < r:
                if stack[l][0] == arr[r]:
                    ll = stack[l][1] + 1
                elif stack[l][0] < arr[r]:
                    ll = stack[l][1] + 1
                else:
                    ll = stack[l][1]
                ans = min(ans, r-ll)
            elif stack and l == len(stack):
                ll = stack[l-1][1] + 1
                ans = min(ans, r-ll)
            r -= 1
            if arr[r] > arr[r+1]:
                break
        return ans
