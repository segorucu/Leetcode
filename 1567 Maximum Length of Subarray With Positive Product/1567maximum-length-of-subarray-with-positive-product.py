class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        arrs = []
        curr = []
        for num in nums:
            if num == 0:
                if curr:
                    arrs.append(curr[:])
                curr = []
            else:
                if num > 0:
                    curr.append(1)
                else:
                    curr.append(-1)
        if curr:
            arrs.append(curr)
        # print(arrs)
        ans = 0
        for arr in arrs:
            negatives = arr.count(-1)
            if negatives % 2 == 0:
                ans = max(ans, len(arr))
            else:
                for i in range(len(arr)):
                    if arr[i] == -1:
                        ans = max(ans, len(arr) - i - 1)
                        break
                for i in range(len(arr)-1,-1,-1):
                    if arr[i] == -1:
                        ans = max(ans, i)
                        break

        return ans



        return 0