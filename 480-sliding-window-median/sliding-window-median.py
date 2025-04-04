from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        n = len(nums)
        ans = []
        arr = SortedList()

        if k % 2:
            med = k // 2
        else:
            medl = k // 2 - 1
            medr = medl + 1

        for i,num in enumerate(nums):
            arr.add(num)
            if i >= k:
                arr.remove(nums[i-k])
            # print(arr)
            if i >= k-1:
                if k % 2:
                    ans.append(arr[med])
                else:
                    tmp = (arr[medl] + arr[medr]) / 2
                    ans.append(tmp)

        return ans
                    


        return ans
