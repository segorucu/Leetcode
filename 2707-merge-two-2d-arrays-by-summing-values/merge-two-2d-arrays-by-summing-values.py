class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        counter = defaultdict(int)
        for i, num in nums1:
            counter[i] += num
        for i, num in nums2:
            counter[i] += num

        arr = [[key,val] for key,val in counter.items()]
        arr.sort()

        return arr