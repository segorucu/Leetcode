class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        graph = defaultdict(int)
        for i,num in enumerate(nums1):
            graph[num] = i

        n = len(nums1)
        array = n * [0]
        for i,num in enumerate(nums2):
            array[i] = graph[num]

        smaller = n * [0]
        left = SortedList()
        for i,num in enumerate(array):
            j = left.bisect(num)
            smaller[i] = j
            left.add(num)
        
        larger = n * [0]
        right = SortedList()
        for i in range(n-1,-1,-1):
            num = array[i]
            j =  right.bisect(-num)
            larger[i] = j
            right.add(-num)

        count = 0
        for i in range(1,n-1):
            count += smaller[i] * larger[i]
        return count