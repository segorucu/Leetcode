class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        positives = collections.deque()
        negatives = collections.deque()

        for i,num in enumerate(nums):
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)
        for i, num in enumerate(nums):
            if i % 2 == 0:
                dum = positives.popleft()
            else:
                dum = negatives.popleft()
            nums[i] = dum

        return nums
        