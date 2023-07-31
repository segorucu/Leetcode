# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        left = 0
        right = reader.length() -1 
        while left <= right:
            odd = (right + left) % 2 == 1
            mid = (right + left) // 2
            if odd:
                midp = mid + 1
            else:
                midp = mid
            
            ans = reader.compareSub(left,mid,midp,right)
            if ans == 0:
                return mid
            elif ans == 1:
                # if odd:
                #     right = midp - 1
                # else:
                right = midp - 1
            else:
                left = mid + 1
            
        return left