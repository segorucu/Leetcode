class SparseVector:
    def __init__(self, nums: List[int]):
        self.mp = collections.defaultdict(int)
        for i,num in enumerate(nums):
            if num == 0:
                continue
            self.mp[i] = num
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        common = self.mp.keys() and vec.mp.keys()
        ans = 0
        for k in common:
            ans += self.mp[k] * vec.mp[k]
        return ans
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)