class Solution:
    def maximumBinaryString(self, binary: str) -> str:

        n = len(binary)
        N0 = binary.count("0")
        if N0 == 0:
            return binary
        first0 = binary.index("0")
        n1 = first0 + N0 - 1
        n2 = n - n1 - 1
        ans = n1*"1" + "0" + n2*"1"

        return ans
        