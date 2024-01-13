class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y

        sm = 0
        while z > 0:
            sm += z & 1
            z = z >> 1
        return sm

        