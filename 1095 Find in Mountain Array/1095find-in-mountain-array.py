# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        n = mountain_arr.length()
        
        l = 1
        r = n-2
        

        while l <= r:
            mid = (l+r) // 2
            curr = mountain_arr.get(mid)
            currl = mountain_arr.get(mid-1)
            currr = mountain_arr.get(mid+1)
            if currl < curr and curr > currr:
                peak = curr
                peakind = mid
                break
            elif currl < curr < currr:
                l = mid + 1
            else:
                r = mid - 1

        l = 0
        r = peakind
        while l <= r:
            mid = (l+r) // 2
            curr = mountain_arr.get(mid)
            if curr == target:
                return mid
            elif curr < target:
                l = mid + 1
            else:
                r = mid - 1

        l = peakind
        r = n-1
        while l <= r:
            mid = (l+r) // 2
            curr = mountain_arr.get(mid)
            if curr == target:
                return mid
            elif curr > target:
                l = mid + 1
            else:
                r = mid - 1

        return -1
            

        
        


        return -1
