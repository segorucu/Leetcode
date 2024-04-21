class Solution:
    def average(self, salary: List[int]) -> float:

        sm = 0
        minval = inf
        maxval = -inf
        for val in salary:
            sm += val
            if val > maxval:
                maxval = val
            if val < minval:
                minval = val

        sm = sm - maxval - minval
        return sm / (len(salary)-2)
        