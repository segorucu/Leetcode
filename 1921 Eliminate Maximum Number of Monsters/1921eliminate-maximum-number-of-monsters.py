class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        time = []
        for d,s in zip(dist,speed):
            time.append(d/s)
        time.sort()

        for i, ti in enumerate(time):
            if i >= ti:
                return i
        return len(time)
        