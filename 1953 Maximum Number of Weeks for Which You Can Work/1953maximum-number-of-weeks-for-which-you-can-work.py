class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:

        n = len(milestones)
        if n == 1:
            return 1

        sm = sum(milestones)
        maxval = max(milestones)
        first = sm - maxval

        if first >= maxval - 1:
            return sm
        else:
            return 2*first+1
        