class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        left_id = right_id = bad_id = -1
        count = 0
        for i, num in enumerate(nums):

            if not (minK <= num <= maxK):
                bad_id = i

            if num == minK:
                left_id = i

            if num == maxK:
                right_id = i

            count += max(0,min(left_id,right_id) - bad_id)

        return count

        