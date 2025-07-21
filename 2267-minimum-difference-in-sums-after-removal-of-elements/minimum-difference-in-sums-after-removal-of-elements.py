from sortedcontainers import SortedList
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        
        n = len(nums)
        k = n // 3
        rightside = SortedList()
        leftside = SortedList()
        temporary = SortedList()
        for i in range(n):
            if i < k:
                leftside.add(nums[i])
            else:
                rightside.add(nums[i])
                if len(rightside) > k:
                    tmp = rightside.pop(0)
                    temporary.add(tmp)
        
        rightsm = sum(rightside)
        leftsm = sum(leftside)
        ans = leftsm - rightsm
        
        for r in range(k, n-k):
            to_be_removed = nums[r]
            if to_be_removed in temporary:
                temporary.remove(to_be_removed)
            else:
                rightside.remove(to_be_removed)
                rightsm -= to_be_removed
                tmp = temporary.pop()
                rightside.add(tmp)
                rightsm += tmp

            leftside.add(to_be_removed)
            leftsm += to_be_removed
            tmp = leftside.pop()
            leftsm -= tmp
            ans = min(ans, leftsm - rightsm)
            # print(leftsm, rightsm)


        return ans


