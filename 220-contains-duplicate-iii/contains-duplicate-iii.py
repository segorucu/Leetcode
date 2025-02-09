from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        
        rightside = SortedList()
        leftside = SortedList()
        n = len(nums)

        for i in range(1,min(indexDiff+1,n)):
            rightside.add(nums[i])

        for i in range(n):
            # print("i",i)
            # print("rightside",rightside)
            # print("leftside",leftside)
            # check left and right lists
            if rightside:
                ind = rightside.bisect_left(nums[i])
                ind = min(ind,len(rightside)-1)
                if abs(rightside[ind]-nums[i]) <= valueDiff:
                    return True
            if leftside:
                ind = leftside.bisect_left(nums[i])
                ind = min(ind,len(leftside)-1)
                if abs(leftside[ind]-nums[i]) <= valueDiff:
                    return True
            
            #update sorted lists
            leftside.add(nums[i])

            leftp = i - indexDiff
            if leftp >= 0:
                leftside.remove(nums[leftp])

            if i + 1 < n:
                rightside.remove(nums[i+1])

            rightp = i + indexDiff + 1
            if rightp < n:
                rightside.add(nums[rightp])

        return False