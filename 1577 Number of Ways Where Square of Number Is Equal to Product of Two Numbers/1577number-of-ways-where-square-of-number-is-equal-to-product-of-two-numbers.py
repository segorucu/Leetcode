class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        sq1 = collections.defaultdict(int)
        for num in nums1:
            sq1[num**2] += 1
        sq2 = collections.defaultdict(int)
        for num in nums2:
            sq2[num**2] += 1

        m = len(nums1)
        n = len(nums2)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                ans += sq1[nums2[i]*nums2[j]]
        for i in range(m):
            for j in range(i+1,m):
                ans += sq2[nums1[i]*nums1[j]]
        return ans
        

        