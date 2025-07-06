class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.c1 = Counter(nums1)
        self.nums1 = nums1
        self.nums2 = nums2
        self.c2 = Counter(nums2)
        

    def add(self, index: int, val: int) -> None:
        prev = self.nums2[index]
        self.c2[prev] -= 1
        prev += val
        self.nums2[index] = prev
        self.c2[prev] += 1
        
    def count(self, tot: int) -> int:
        cnt = 0
        for num in self.nums1:
            cnt += self.c2[tot-num]
        return cnt
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)